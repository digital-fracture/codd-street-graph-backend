from sqlalchemy import Integer, String, Uuid, JSON, ForeignKey
from sqlalchemy.orm import mapped_column

from data.database import Base


class Upload(Base):
    __tablename__ = "uploads"

    upload_id = mapped_column(Uuid, primary_key=True)
    user_id = mapped_column(Uuid, nullable=False, index=True)
    version = mapped_column(Integer, nullable=False, index=True)
    path = mapped_column(String, nullable=False)


class Graph(Base):
    __tablename__ = "graphs"

    upload_id = mapped_column(ForeignKey("uploads.upload_id"), primary_key=True)
    parameters = mapped_column(String, primary_key=True)
    graph = mapped_column(JSON)
