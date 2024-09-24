from dynaconf import Dynaconf
from pathlib import Path


project_root_directory = Path(__file__).resolve().parent.parent.parent
settings_path = project_root_directory / 'settings.toml'

settings = Dynaconf(
    envvar_prefix="SERVICE",
    settings_files=[settings_path, '.secrets.toml'],
    environment=True,
    load_doenv=True,
    env_switcher="SERVICE_ENV"
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
