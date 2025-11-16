from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# Не меняйте эти три строки:
app = FastAPI()
engine = create_async_engine(url='sqlite+aiosqlite:///secret_db.sqlite3')
Sessionmaker = async_sessionmaker(engine, expire_on_commit=False)


# Этот класс трогать не надо.
class Base(DeclarativeBase):
    pass


class SecretMessage(BaseModel):
    # Опишите Pydantic-схему для зашифрованных сообщений.
    # Все поля - обязательные.
    title: str
    message: str


class ReadyNews(Base):
    # Опишите модель для хранения данных в БД.
    # Дополнительных классов создавать не нужно.
    # Таблицу назовите `news`.
    __tablename__ = 'news'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    message: Mapped[str] = mapped_column(String, nullable=False)


def decoder(data: dict[str, str]) -> dict[str, str]:
    """
    Сверхсекретный декодер.
    Здесь всё работает, ничего менять не надо!
    """
    decoded_data = {}
    for key, value in data.items():
        decoded_str = (chr(int(chunk)) for chunk in value.split('-'))
        decoded_data[key] = ''.join(decoded_str)
    return decoded_data


@app.post('/super-secret-base')
async def receiver(encoded_news: SecretMessage):
    # Передайте сообщение в декодер.
    secret = decoder(encoded_news.model_dump())

    # Создайте переменную ready_news - объект класса ReadyNews
    # из декодированного сообщения.
    ready_news = ReadyNews(**secret)
    # Получите асинхронную сессию из Sessionmaker,
    # добавьте в неё объект ReadyNews и сохраните данные в БД.
    async with Sessionmaker() as session:
        session.add(ready_news)
        await session.commit()

    # Верните объект класса ReadyNews.
    return ready_news