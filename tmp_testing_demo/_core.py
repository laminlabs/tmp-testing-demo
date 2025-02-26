import lamindb as ln
import pandas as pd


def save_dataframe(df: pd.DataFrame, description: str) -> ln.Artifact:
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
