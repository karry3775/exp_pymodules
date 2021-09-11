import pytest
from grep_func import grep_func
from io import BytesIO
import sys
import re
from colorama import Fore


def test_grep():
    import logging

    pattern = "basic"

    sys.stdout = BytesIO()

    grep_func.grep_func(logging, pattern)

    out_val = str(sys.stdout.getvalue())

    sys.stdout = sys.__stdout__  # restores original stdout

    val = (
        re.sub(r"({})".format(pattern), Fore.RED + r"\1" + Fore.RESET, "basicConfig")
        + "\n"
    )
    assert out_val == val
