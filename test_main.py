import pytest

import main


class TestCheckNavdata:
    @pytest.mark.parametrize("navdata,expected", (
            ("()", 0),
            ("(]", 57),
            ("({([(<{}[<>[]}>{[]{[(<()>", 1197),
            ("[[<[([]))<([[{}[[()]]]", 3),
            ("[{[{({}]{}}([{[{{{}}([]", 57),
            ("[<(<(<(<{}))><([]([]()", 3),
            ("<{([([[(<>()){}]>(<<{{", 25137)
    ))
    def test_check_navdata_validates_correctly(self, navdata, expected):
        assert main.check_navdata(navdata) == expected
