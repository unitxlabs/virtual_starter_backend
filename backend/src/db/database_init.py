from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_NAME = "virtual_hardware"
USERNAME = "postgres"
PASSWORD = "mysecretpassword"
LOCAL_HOST = "localhost"
ECHO_LOG = False


DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{LOCAL_HOST}/{DATABASE_NAME}"

initial_engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{LOCAL_HOST}/postgres")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database(engine, db_name):
    """Create a new database."""
    with engine.connect() as conn:
        conn.execute(text("COMMIT"))
        conn.execute(text(f"CREATE DATABASE {db_name}"))
        conn.execute(text("COMMIT"))


def database_exists(engine, db_name) -> bool:
    """Check if a database exists."""
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'"))
        return bool(result.scalar())


if __name__ == "__main__":
    if not database_exists(initial_engine, DATABASE_NAME):
        create_database(initial_engine, DATABASE_NAME)
        print("Database initialized")
    print("Database exists")
