from cc_uv_test.foo import bar, foo


def test_foo():
    assert foo("foo") == "foo"


def test_bar():
    assert bar() == "bar"
