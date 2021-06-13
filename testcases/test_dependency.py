import pytest


@pytest.mark.dependency()
def test_b():
    # pass
    assert False


@pytest.mark.dependency(depends=["test_b"])
def test_c():
    pass
