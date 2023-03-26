import unittest
from unittest.mock import MagicMock

from src import parse


class TestParseMethods(unittest.TestCase):
    def test_parse_makes(self):
        TEST_URL = "abc"
        TEST_RESPONSE = "test"

        TARGET0 = "<a class=\"megamenu-in-page__link\" href=\""
        TARGET1 = "\">"

        rmote = MagicMock()
        rmote.pull = MagicMock(return_value=TARGET0+TEST_RESPONSE+TARGET1)
        parser = parse.Parser(remote=rmote)

        assert parser.parse_makes(TEST_URL) == [TEST_RESPONSE]

    def test_parse_models(self):
        TEST_URL = "abc"
        TEST_RESPONSE = "test"

        TARGET0 = "<a class=\"text-uppercase link link--blue\" href=\""
        TARGET1 = "\">"

        rmote = MagicMock()
        rmote.pull = MagicMock(return_value=TARGET0+TEST_RESPONSE+TARGET1)
        parser = parse.Parser(remote=rmote)

        assert parser.parse_models(TEST_URL) == [TEST_RESPONSE]

    def test_parse_specs(self):
        TEST_URL = "abc"
        TEST_RESPONSE_A = "testA"
        TEST_RESPONSE_B = "testB"

        TARGET0 = "<div class=\"stats__list__accordion__body__stat__top__title\">"
        TARGET1 = "</div>"
        TARGET2 = "class=\"stats__list__accordion__body__stat__top__right__stat-time\">"
        TARGET3 = " <span"

        rmote = MagicMock()
        rmote.pull = MagicMock(return_value=TARGET0+TEST_RESPONSE_A+TARGET1+TARGET2+TEST_RESPONSE_B+TARGET3)
        parser = parse.Parser(remote=rmote)

        assert parser.parse_specs(TEST_URL) == [TEST_RESPONSE_A+":"+TEST_RESPONSE_B]

    def test_stepover(self):
        TEST_HYPERTEXT = "abcdefg"

        rmote = MagicMock()
        rmote.pull = MagicMock(return_value=b"")
        parser = parse.Parser(remote=rmote)

        data, hypertext = parser._stepover(TEST_HYPERTEXT, "a", "d")
        assert data == "bc"
        assert hypertext == "defg"

    def test_stepover_error_missing_targets(self):
        TEST_HYPERTEXT = "abcdefg"

        rmote = MagicMock()
        rmote.pull = MagicMock(return_value=b"")
        parser = parse.Parser(remote=rmote)

        with self.assertRaises(ValueError):
            parser._stepover(TEST_HYPERTEXT, "h", "m")

    def test_stepover_error_missing_target1(self):
        TEST_HYPERTEXT = "abcdefg"

        rmote = MagicMock()
        rmote.pull = MagicMock(return_value=b"")
        parser = parse.Parser(remote=rmote)

        with self.assertRaises(ValueError):
            parser._stepover(TEST_HYPERTEXT, "m", "f")

    def test_stepover_error_missing_target2(self):
        TEST_HYPERTEXT = "abcdefg"

        rmote = MagicMock()
        rmote.pull = MagicMock(return_value=b"")
        parser = parse.Parser(remote=rmote)

        with self.assertRaises(ValueError):
            parser._stepover(TEST_HYPERTEXT, "f", "m")


if __name__ == '__main__':
    unittest.main()
