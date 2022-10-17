from typing import Generator


def get_db() -> Generator:
    try:
        db = SesisonLocal()
        yield db
    finally:
        db.close()
