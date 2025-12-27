from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.profile import ProfileCreate, ProfileUpdate, ProfileRead, DeleteResponse
from ..services.profile_service import ProfileService

router = APIRouter(prefix="/profiles", tags=["profiles"])


def calculate_age(date_of_birth: date) -> int:
    """Calculate age from date of birth"""
    today = date.today()
    age = today.year - date_of_birth.year
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1
    return age


def model_to_schema(model) -> ProfileRead:
    """Convert SQLAlchemy model to Pydantic schema with derived age"""
    return ProfileRead(
        id=model.id,
        gender=model.gender,
        title=model.title,
        firstName=model.first_name,
        lastName=model.last_name,
        dateOfBirth=model.date_of_birth,
        age=calculate_age(model.date_of_birth),
        pictureLarge=model.picture_large,
        pictureThumbnail=model.picture_thumbnail,
        streetNumber=model.street_number,
        streetName=model.street_name,
        city=model.city,
        state=model.state,
        country=model.country,
        email=model.email,
        phone=model.phone,
    )


@router.get("", response_model=list[ProfileRead])
def get_profiles(db: Session = Depends(get_db)):
    service = ProfileService(db)
    profiles = service.get_all()
    return [model_to_schema(p) for p in profiles]


@router.get("/{profile_id}", response_model=ProfileRead)
def get_profile(profile_id: str, db: Session = Depends(get_db)):
    service = ProfileService(db)
    profile = service.get_by_id(profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return model_to_schema(profile)


@router.post("", response_model=ProfileRead)
def create_profile(data: ProfileCreate, db: Session = Depends(get_db)):
    service = ProfileService(db)
    profile = service.create(data)
    return model_to_schema(profile)


@router.put("/{profile_id}", response_model=ProfileRead)
def update_profile(profile_id: str, data: ProfileUpdate, db: Session = Depends(get_db)):
    print(f"[UPDATE] profile_id={profile_id}, firstName={data.firstName}, lastName={data.lastName}")
    service = ProfileService(db)
    profile = service.update(profile_id, data)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    print(f"[UPDATE] Success: {profile.first_name} {profile.last_name}")
    return model_to_schema(profile)


@router.delete("/{profile_id}", response_model=DeleteResponse)
def delete_profile(profile_id: str, db: Session = Depends(get_db)):
    service = ProfileService(db)
    success = service.delete(profile_id)
    if not success:
        raise HTTPException(status_code=404, detail="Profile not found")
    return DeleteResponse(success=True)
