from datetime import date
from pydantic import BaseModel


class ProfileCreate(BaseModel):
    """Schema for creating a new profile"""
    gender: str
    # Name
    title: str
    firstName: str
    lastName: str
    # Date of birth
    dateOfBirth: date
    # Picture
    pictureLarge: str
    pictureThumbnail: str
    # Address
    streetNumber: int
    streetName: str
    city: str
    state: str
    country: str
    # Contact
    email: str
    phone: str


class ProfileUpdate(BaseModel):
    """Schema for updating a profile"""
    gender: str
    # Name
    title: str
    firstName: str
    lastName: str
    # Date of birth
    dateOfBirth: date
    # Picture
    pictureLarge: str
    pictureThumbnail: str
    # Address
    streetNumber: int
    streetName: str
    city: str
    state: str
    country: str
    # Contact
    email: str
    phone: str


class ProfileRead(BaseModel):
    """Schema for reading a profile (includes id and derived age)"""
    id: str
    gender: str
    # Name
    title: str
    firstName: str
    lastName: str
    # Date of birth and derived age
    dateOfBirth: date
    age: int  # Derived from dateOfBirth
    # Picture
    pictureLarge: str
    pictureThumbnail: str
    # Address
    streetNumber: int
    streetName: str
    city: str
    state: str
    country: str
    # Contact
    email: str
    phone: str

    model_config = {"from_attributes": True}


class DeleteResponse(BaseModel):
    success: bool
