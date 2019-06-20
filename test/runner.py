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

import os

import six

import test

if six.PY2:
    import unittest2 as unittest
else:
    import unittest

# set EXTENDED_TEST from env
if os.environ.get('EXTENDED_TEST'):
    test.api_tester.ApiTester.EXTENDED_TEST = os.environ.get('EXTENDED_TEST')

loader = unittest.TestLoader()

suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(test.test_compare_images))
suite.addTests(loader.loadTestsFromModule(test.test_find_duplicates))
suite.addTests(loader.loadTestsFromModule(test.test_find_images))
suite.addTests(loader.loadTestsFromModule(test.test_search_context))
suite.addTest(loader.loadTestsFromModule(test.test_file_api))
suite.addTest(loader.loadTestsFromModule(test.test_folder_api))
suite.addTest(loader.loadTestsFromModule(test.test_storage_api))
suite.addTest(loader.loadTestsFromModule(test.test_bmp_api))
suite.addTest(loader.loadTestsFromModule(test.test_crop_api))
suite.addTest(loader.loadTestsFromModule(test.test_emf_api))
suite.addTest(loader.loadTestsFromModule(test.test_examples))
suite.addTest(loader.loadTestsFromModule(test.test_frames_get_api))
suite.addTest(loader.loadTestsFromModule(test.test_frames_post_api))
suite.addTest(loader.loadTestsFromModule(test.test_gif_api))
suite.addTest(loader.loadTestsFromModule(test.test_jpeg2000_api))
suite.addTest(loader.loadTestsFromModule(test.test_jpg_api))
suite.addTest(loader.loadTestsFromModule(test.test_psd_api))
suite.addTest(loader.loadTestsFromModule(test.test_resize_api))
suite.addTest(loader.loadTestsFromModule(test.test_rotate_flip_api))
suite.addTest(loader.loadTestsFromModule(test.test_save_as_api))
suite.addTest(loader.loadTestsFromModule(test.test_tiff_api))
suite.addTest(loader.loadTestsFromModule(test.test_update_image_api))
suite.addTest(loader.loadTestsFromModule(test.test_web_p_api))
suite.addTest(loader.loadTestsFromModule(test.test_wmf_api))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
