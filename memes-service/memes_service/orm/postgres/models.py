from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Meme(Base):
    __tablename__ = 'meme'

    id = mapped_column(Integer, primary_key=True)
    content = mapped_column(String(256), nullable=False)
    img_url = mapped_column(String(256), nullable=True)
