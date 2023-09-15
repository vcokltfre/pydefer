from defer import defer, use_defer


@use_defer
def test() -> None:
    print("test")           # first
    defer(print, "defered") # third
    print("test end")       # second


test()
