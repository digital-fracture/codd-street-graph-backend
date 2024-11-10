from sqlalchemy import Integer, String, Uuid, JSON
from sqlalchemy.orm import mapped_column

from data.database import Base


class Upload(Base):
    __tablename__ = "uploads"

    user_id = mapped_column(Uuid, primary_key=True)
    version = mapped_column(Integer, primary_key=True)
    path = mapped_column(String, nullable=False)
    json_data = mapped_column(JSON)
