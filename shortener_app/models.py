from sqlalchemy import Column, Integer, String
from shortener_app.database import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    url = Column(String, index=True)
