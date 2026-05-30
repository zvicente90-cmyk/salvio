import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Load .env for local development if present
try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
except Exception:
    pass

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Ensure project root is importable (so `backend` package can be imported)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Import your models' MetaData object so Alembic can autogenerate migrations
try:
    from backend.app.models.base import Base  # type: ignore
    # Importing models package ensures all model modules are loaded and registered
    from backend.app.models import *  # noqa: F401,F403
    target_metadata = Base.metadata
except Exception:
    target_metadata = None

# Read DB URL from env (recommended). Fallback to sqlalchemy.url in alembic.ini
DATABASE_URL = os.getenv('DATABASE_URL') or config.get_main_option('sqlalchemy.url')
if DATABASE_URL:
    config.set_main_option('sqlalchemy.url', DATABASE_URL)


def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section) if config.config_ini_section else {},
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
