from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from lib.database import Base  # Import Base for model metadata
from lib.database import engine  # Import engine to use in online migrations

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers as defined in alembic.ini.
fileConfig(config.config_file_name)

# Add your model's MetaData object here
# for 'autogenerate' support. This allows Alembic to
# generate migrations based on model changes.
target_metadata = Base.metadata

# Run migrations in 'offline' mode.
def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    # Configure the context to use the database URL from the config.
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,  # Use literal binds for parameterized queries
        dialect_opts={"paramstyle": "named"},  # Parameterized query style
    )

    # Begin and run the migrations offline
    with context.begin_transaction():
        context.run_migrations()


# Run migrations in 'online' mode.
def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Create an engine from the config
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",  # Use 'sqlalchemy.' as the prefix for config values
        poolclass=pool.NullPool,  # No connection pooling
    )

    # Establish a connection and run migrations
    with connectable.connect() as connection:
        context.configure(
            connection=connection,  # Use the connection to configure Alembic
            target_metadata=target_metadata
        )

        # Begin and run the migrations online
        with context.begin_transaction():
            context.run_migrations()


# Check if we are in offline mode or online mode and run the respective function.
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()