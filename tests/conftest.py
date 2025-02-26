import lamindb_setup as ln_setup
import pytest


@pytest.fixture(scope="session")
def setup_instance():
    ln_setup.init(storage="./testdb", modules="bionty")
    yield
    ln_setup.delete("testdb", force=True)
