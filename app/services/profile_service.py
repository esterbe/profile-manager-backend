import uuid
from sqlalchemy.orm import Session
from ..models.profile import Profile as ProfileModel
from ..schemas.profile import ProfileCreate, ProfileUpdate


class ProfileService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[ProfileModel]:
        return self.db.query(ProfileModel).all()

    def get_by_id(self, profile_id: str) -> ProfileModel | None:
        return self.db.query(ProfileModel).filter(ProfileModel.id == profile_id).first()

    def create(self, data: ProfileCreate) -> ProfileModel:
        profile = ProfileModel(
            id=str(uuid.uuid4()),
            gender=data.gender,
            title=data.title,
            first_name=data.firstName,
            last_name=data.lastName,
            date_of_birth=data.dateOfBirth,
            picture_large=data.pictureLarge,
            picture_thumbnail=data.pictureThumbnail,
            street_number=data.streetNumber,
            street_name=data.streetName,
            city=data.city,
            state=data.state,
            country=data.country,
            email=data.email,
            phone=data.phone,
        )
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile

    def update(self, profile_id: str, data: ProfileUpdate) -> ProfileModel | None:
        profile = self.get_by_id(profile_id)
        if not profile:
            return None

        profile.gender = data.gender
        profile.title = data.title
        profile.first_name = data.firstName
        profile.last_name = data.lastName
        profile.date_of_birth = data.dateOfBirth
        profile.picture_large = data.pictureLarge
        profile.picture_thumbnail = data.pictureThumbnail
        profile.street_number = data.streetNumber
        profile.street_name = data.streetName
        profile.city = data.city
        profile.state = data.state
        profile.country = data.country
        profile.email = data.email
        profile.phone = data.phone

        self.db.commit()
        self.db.refresh(profile)
        return profile

    def delete(self, profile_id: str) -> bool:
        profile = self.get_by_id(profile_id)
        if not profile:
            return False

        self.db.delete(profile)
        self.db.commit()
        return True
