from datetime import date
from pydantic import BaseModel


class ProfileCreate(BaseModel):
    """Schema for creating a new profile"""
    gender: str
    title: str
    firstName: str
    lastName: str
    dateOfBirth: date
    pictureLarge: str
    pictureThumbnail: str
    streetNumber: int
    streetName: str
    city: str
    state: str
    country: str
    email: str
    phone: str


class ProfileUpdate(BaseModel):
    """Schema for updating a profile"""
    gender: str
    title: str
    firstName: str
    lastName: str
    dateOfBirth: date
    pictureLarge: str
    pictureThumbnail: str
    streetNumber: int
    streetName: str
    city: str
    state: str
    country: str
    email: str
    phone: str


class ProfileRead(BaseModel):
    """Schema for reading a profile (includes id and derived age)"""
    id: str
    gender: str
    title: str
    firstName: str
    lastName: str
    dateOfBirth: date
    age: int  # Derived from dateOfBirth
    pictureLarge: str
    pictureThumbnail: str
    streetNumber: int
    streetName: str
    city: str
    state: str
    country: str
    email: str
    phone: str

    model_config = {"from_attributes": True}


class DeleteResponse(BaseModel):
    success: bool
