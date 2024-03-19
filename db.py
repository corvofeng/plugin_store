
import datetime

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.types import Boolean, Date, DateTime, Float, Integer, Text, Time, Interval

class Base(DeclarativeBase):
    pass

class WechatMessages(Base):
    __tablename__ = "wechat_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[str] = mapped_column(String(30), index=True)
    sender_name: Mapped[str] = mapped_column(String(30), index=True)
    receiver_id: Mapped[Optional[str]] = mapped_column(String(30), index=True)
    receiver_name: Mapped[Optional[str]] = mapped_column(String(30), index=True)
    room_id: Mapped[str] = mapped_column(String(30), index=True)

    content: Mapped[Optional[str]] = mapped_column(String(10240))
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime())
#     created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # def __repr__(self) -> str:
    #     return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

