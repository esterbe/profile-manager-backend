import uuid
from sqlalchemy import Column, String, Integer, Date
from ..database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    gender = Column(String, nullable=False)

    title = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    date_of_birth = Column(Date, nullable=False)

    picture_large = Column(String, nullable=False)
    picture_thumbnail = Column(String, nullable=False)

    street_number = Column(Integer, nullable=False)
    street_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)

    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
