from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


def use_defer(func: Callable[P, T]) -> Callable[P, T]:
    """Allows the use of defer() within the wrapped function."""

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        defers: list[tuple[Callable[..., Any], Any, Any]] = []

        def _defer(func: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
            defers.append((func, args, kwargs))

        func.__globals__["defer"] = _defer

        val = func(*args, **kwargs)

        for f, args, kwargs in reversed(defers):
            f(*args, **kwargs)

        return val

    return wrapper


def defer(func: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
    """Used to satisfy the type checker when using use_defer()."""

    pass
