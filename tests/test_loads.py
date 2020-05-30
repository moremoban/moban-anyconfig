import os

from moban_anyconfig.adapter import loads

from nose.tools import eq_


def test_toml():
    content = loads(os.path.join("tests", "fixtures", "test.toml"))
    expected = {
        "title": "TOML Example",
        "owner": {"name": "Tom Preston-Werner"},
    }
    eq_(content, expected)
