import pytest

import main


class TestCheckNavdata:
    @pytest.mark.parametrize("navdata,expected", (("()", True), ("[]", True), ("(]", False), ("(()[])", True), "[)"))
    def test_check_navdata_validates_correctly(self, navdata, expected):
        result = main.check_navdata(navdata)
        assert result is expected
