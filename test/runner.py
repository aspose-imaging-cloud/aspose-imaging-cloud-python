#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="runner.py">
#    Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
#  </copyright>
#  <summary>
#    Permission is hereby granted, free of charge, to any person obtaining a
#   copy  of this software and associated documentation files (the "Software"),
#   to deal  in the Software without restriction, including without limitation
#   the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell  copies of the Software, and to permit persons to whom the
#   Software is  furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all  copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#  </summary>
#  ----------------------------------------------------------------------------

import argparse
import os
import sys
from distutils.util import strtobool

import six
import xmlrunner

import test

if six.PY2:
    import unittest2 as unittest
else:
    import unittest

# runner works with one optional argument - directory to save test results
parser = argparse.ArgumentParser(
    description='Test Aspose Imaging Cloud SDK for Python')
parser.add_argument(
    '-o', '--output_directory', default=None, required=False,
    help='Directory to save test results. '
         'Test result are not saved by default.')
args = parser.parse_args()

# set EXTENDED_TEST from env
if os.environ.get('ExtendedTests'):
    test.api_tester.ApiTester.EXTENDED_TEST = bool(
        strtobool((os.environ.get('ExtendedTests'))))

# get test categories from env
test_categories = None
if os.environ.get('TestCategories'):
    test_categories = os.environ.get('TestCategories')

# Test categories can't be managed by framework so they should be collected
# here manually
loader = unittest.TestLoader()
suites_dict = {}

# TODO: move test discovery to lambda to discovery only required categories?
ai_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.AI.test_compare_images']))
ai_suite.addTests(loader.loadTestsFromModule(
    sys.modules['test.api.AI.test_find_duplicates']))
ai_suite.addTests(
    loader.loadTestsFromModule(sys.modules['test.api.AI.test_find_images']))
ai_suite.addTests(
    loader.loadTestsFromModule(sys.modules['test.api.AI.test_search_context']))
suites_dict['Ai'] = ai_suite

objectdetection_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.AI.test_objectdetection_api']))
suites_dict['ObjectDetection'] = objectdetection_suite

file_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.storage.test_file_api']))
suites_dict['File'] = file_suite

filter_effect_suite = unittest.TestSuite(loader.loadTestsFromModule(
    sys.modules['test.api.test_filter_effect_api']))
suites_dict['FilterEffect'] = filter_effect_suite

folder_suite = unittest.TestSuite(loader.loadTestsFromModule(
    sys.modules['test.api.storage.test_folder_api']))
suites_dict['Folder'] = folder_suite

storage_suite = unittest.TestSuite([file_suite, folder_suite])
storage_suite.addTests(loader.loadTestsFromModule(
    sys.modules['test.api.storage.test_storage_api']))
suites_dict['Storage'] = storage_suite

bmp_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_bmp_api']))
suites_dict['Bmp'] = bmp_suite

crop_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_crop_api']))
suites_dict['Crop'] = crop_suite

emf_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_emf_api']))
suites_dict['Emf'] = emf_suite

examples_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_examples']))
suites_dict['Examples'] = examples_suite

tiff_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_tiff_api']))
suites_dict['Tiff'] = tiff_suite

gif_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_gif_api']))
suites_dict['Gif'] = gif_suite

jpeg2000_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_jpeg2000_api']))
suites_dict['jpeg2000'] = jpeg2000_suite

jpg_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_jpg_api']))
suites_dict['jpg'] = jpg_suite

psd_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_psd_api']))
suites_dict['Psd'] = psd_suite

resize_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_resize_api']))
suites_dict['Resize'] = resize_suite

rotate_flip_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_rotate_flip_api']))
suites_dict['RotateFlip'] = rotate_flip_suite

convert_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_convert_api']))
suites_dict['Convert'] = convert_suite

svg_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_svg_api']))
suites_dict['Svg'] = svg_suite

frames_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_frames_api']))
suites_dict['Frames'] = frames_suite

update_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_update_image_api']))
suites_dict['Update'] = update_suite

web_p_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_web_p_api']))
suites_dict['Webp'] = web_p_suite

wmf_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_wmf_api']))
suites_dict['Wmf'] = wmf_suite

load_custom_fonts_suite = unittest.TestSuite(
    loader.loadTestsFromModule(sys.modules['test.api.test_load_custom_fonts_api']))
suites_dict['LoadCustomFonts'] = load_custom_fonts_suite

imaging_suit = unittest.TestSuite(
    [bmp_suite, crop_suite, emf_suite, examples_suite, tiff_suite, gif_suite,
     jpeg2000_suite, jpg_suite, psd_suite, resize_suite, rotate_flip_suite,
     convert_suite, update_suite, web_p_suite, wmf_suite, load_custom_fonts_suite])
suites_dict['Imaging'] = imaging_suit

v3_suite = unittest.TestSuite(
    [ai_suite, storage_suite, bmp_suite, crop_suite, emf_suite, examples_suite,
     tiff_suite, gif_suite, jpeg2000_suite, jpg_suite, psd_suite, resize_suite,
     rotate_flip_suite, convert_suite, update_suite, web_p_suite, wmf_suite])
suites_dict['v3.0'] = v3_suite

suite = unittest.TestSuite()
if test_categories:
    for category in test_categories.split():
        suite.addTests(suites_dict[category])
else:
    suite.addTests(loader.loadTestsFromModule(sys.modules['test']))

if args.output_directory:
    runner = xmlrunner.XMLTestRunner(output=args.output_directory, verbosity=2)
else:
    runner = unittest.TextTestRunner(verbosity=2)

result = not runner.run(suite).wasSuccessful()
sys.exit(result)
