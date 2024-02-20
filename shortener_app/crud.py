from sqlalchemy.orm import Session
from shortener_app.database import SessionLocal, engine
from shortener_app import models


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_url_info(url, key, db: Session):
    db_url = models.URL(
        target_url=url, key=key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    return key


def get_url(url_key, db: Session):
    db_url = (
        db.query(models.URL)
        .filter(models.URL.key == url_key)
        .first()
    )
    return db_url
