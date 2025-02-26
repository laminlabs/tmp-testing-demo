from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from lamindb import Artifact


def save_dataframe(df: pd.DataFrame, description: str) -> "Artifact":
    # Don't import this at the top level because it requires an instance set up
    import lamindb as ln

    return ln.Artifact.from_df(df, description=description).save()


class ExampleClass:
    """Awesome class."""

    def __init__(self, value: int):
        print("initializing")

    def bar(self) -> str:
        """Bar function."""
        return "hello"

    @property
    def foo(self) -> str:
        """Foo property."""
        return "hello"
