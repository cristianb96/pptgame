import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from dotenv import load_dotenv
from app.models import Base, Player
from app.config import db

load_dotenv()
config = context.config
database_url = os.getenv("DATABASE_URL")#"postgresql://postgres:1234@localhost:5432/TEST_1"
config.set_main_option('sqlalchemy.url', database_url)

target_metadata = db.Model.metadata  #Base.metadata

def run_migrations_offline():
    """Ejecuta migraciones en modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecuta migraciones en modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
