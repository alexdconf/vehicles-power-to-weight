import unittest
from unittest.mock import MagicMock

from src import remote


class TestRemoteMethods(unittest.TestCase):
    def test_pull(self):
        TEST_URL = "abc"
        TEST_RESPONSE = "def"

        rmote = remote.Remote()
        dummy = MagicMock()
        dummy.content = TEST_RESPONSE
        rmote.get = MagicMock(return_value=dummy)
        
        assert rmote.pull(TEST_URL) == TEST_RESPONSE

    def test_pull_timeout_failure(self):
        TEST_URL = "abc"
        TEST_RESPONSE = ""

        rmote = remote.Remote()
        rmote.get = MagicMock(side_effect=ConnectionError())

        assert rmote.pull(TEST_URL, retries=1) == TEST_RESPONSE


if __name__ == '__main__':
    unittest.main()
