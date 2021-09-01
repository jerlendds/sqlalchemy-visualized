from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

if __name__ == "__main__":
    ip = "10.5.0.5"
    postgres_dsn = f"postgresql://postgres:password@{ip}:5432/app"
    engine = create_engine(postgres_dsn)

    Base.metadata.drop_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)  # noqa
