from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import profiles_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Profile Manager API",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with API versioning
app.include_router(profiles_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Profile Manager API", "version": "1.0.0"}


@app.get("/health")
def health():
    return {"status": "healthy"}
