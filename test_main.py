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


class TestRepairNavdata:
    def test_repair_navdata_is_callable(self):
        main.repair_navdata("")

    @pytest.mark.parametrize("navdata,expected", (
            ("([]", ("([])", 1)),
            ("(<{<>}", ("(<{<>}>)", 21)),
            ("[({(<(())[]>[[{[]{<()<>>", ("[({(<(())[]>[[{[]{<()<>>}}]])})]", 288957)),
            ("[(()[<>])]({[<{<<[]>>(", ("[(()[<>])]({[<{<<[]>>()}>]})", 5566)),
            ("(((({<>}<{<{<>}{[]{[]{}", ("(((({<>}<{<{<>}{[]{[]{}}}>}>))))", 1480781)),
            ("{<[[]]>}<{[{[{[]{()[[[]", ("{<[[]]>}<{[{[{[]{()[[[]]]}}]}]}>", 995444)),
            ("<{([{{}}[<[[[<>{}]]]>[]]", ("<{([{{}}[<[[[<>{}]]]>[]]])}>", 294))
    ))
    def test_repair_navdata_completes_line(self, navdata, expected):
        assert main.repair_navdata(navdata) == expected

