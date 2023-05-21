import unittest

from config import PROJECT_ROOT

test_directory = f'{PROJECT_ROOT}/main/web/test_api'
test_suite = unittest.TestLoader().discover(test_directory, pattern='*_test.py')

runner = unittest.TextTestRunner()
runner.run(test_suite)