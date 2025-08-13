from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

from settings.envs import DATABASE_URL, READ_DATABASE_URL


# SQLAlchemy setup
engine = create_engine(
    DATABASE_URL,
    pool_size=1,                            # Minimum number of connections in the pool
    max_overflow=15,                        # Maximum number of connections to allow in overflow
    pool_recycle=30 * 60,                   # Recycle connections after 30 minutes
)
# Create a scoped session factory bound to the engine, with specific session options
session_maker = scoped_session(
    sessionmaker(
        autocommit=False,                   # Disable autocommit mode
        autoflush=False,                    # Disable autoflush mode
        expire_on_commit=False,             # Prevent objects from expiring after commit
        bind=engine                        # Bind the session to the engine
    )
)
# For read operations
read_engine = create_engine(
    READ_DATABASE_URL,
    pool_size=1,                            # Minimum number of connections in the pool
    max_overflow=15,                        # Maximum number of connections to allow in overflow
    pool_recycle=30 * 60,                   # Recycle connections after 30 minutes
)
read_session_maker = scoped_session(
    sessionmaker(
        autocommit=False,                   # Disable autocommit mode
        autoflush=False,                    # Disable autoflush mode
        expire_on_commit=False,             # Prevent objects from expiring after commit
        bind=read_engine                        # Bind the session to the engine
    )
)

# Base class for models
Base = declarative_base()

# Dispose the engine to release resources
engine.dispose()  
read_engine.dispose()

@contextmanager
def get_session():
    """
    Dependency to get a database session
    """
    session = session_maker()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


@contextmanager
def get_read_session():
    """
    Dependency to get a read-only database session
    """
    session = read_session_maker()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
