from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


DB_URL = URL.create(
    drivername="postgresql+asyncpg",
    username="myuser",
    password="mypassword",
    host="localhost",
    port=5432,
    database="redis_test",
)

engine = create_async_engine(
    DB_URL,
    echo=True,
    future=True,
    pool_size=70,
    max_overflow=30,
)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)