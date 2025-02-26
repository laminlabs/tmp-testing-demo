import numpy as np
import pandas as pd


def test_that_uses_instance(setup_instance):
    import lamindb as ln

    df = pd.DataFrame({"a": np.arange(0, 10)})

    af = ln.Artifact.from_df(df, description="test").save()

    # clean up artifacts and stuff that might have side effects
    # generally, be careful with concurrency and try not to write
    # tests that depend on others
    af.delete(permanent=True)
