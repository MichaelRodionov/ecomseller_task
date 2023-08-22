from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from src.config import settings


# ----------------------------------------------------------------
Base = declarative_base()
engine = create_engine(settings.db.url, future=True)


# ----------------------------------------------------------------
def get_session():
    session = Session(engine)
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def get_actual_session():
    return next(get_session())
