import pytest
from grep_func import grep_func
import sys

if sys.version_info[0] == 2:
    from io import BytesIO as StringIO
else:
    from io import StringIO

import re
from colorama import Fore


def test_grep():
    import logging

    pattern = "basic"

    sys.stdout = StringIO()

    grep_func.grep_func(logging, pattern)

    out_val = str(sys.stdout.getvalue())

    sys.stdout = sys.__stdout__  # restores original stdout

    val = (
        re.sub(r"({})".format(pattern), Fore.RED + r"\1" + Fore.RESET, "basicConfig")
        + "\n"
    )
    assert out_val == val
