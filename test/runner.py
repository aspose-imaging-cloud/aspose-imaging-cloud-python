import os
import test
import six
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
