import nox
from laminci.nox import run_pre_commit, run_pytest

nox.options.default_venv_backend = "none"


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


@nox.session()
@nox.parametrize("group", ["unit"])
def build(session, group):
    session.run(*"uv pip install --system -e .[dev]".split())

    if group == "unit":
        run_pytest(session)
