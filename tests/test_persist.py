from io import StringIO
import unittest

from src import persist


class TestPersistMethods(unittest.TestCase):
    def test_persist(self):
        TEST_DATA = {"makes": {"models": ["specs"]}}
        outfile = StringIO()
        
        persister = persist.Persister()
        persister.persist(TEST_DATA, outfile)
        outfile.seek(0)
        content = outfile.read()
        assert content == "make\tmodel\tspecs\nmakes\tmodels\tspecs\n"


if __name__ == '__main__':
    unittest.main()
