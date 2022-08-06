from twttr import shorten
import pytest


def test_twttr_upper_lowcase():
    assert shorten("dwedeef") == "dwdf"

    assert shorten("ASEDKII") == "SDK"


def test_int():
    with pytest.raises(TypeError):
        shorten(3)
def test_num():
    assert shorten("5856") == "5856"

def test_puct():
    assert shorten("?") == "?"