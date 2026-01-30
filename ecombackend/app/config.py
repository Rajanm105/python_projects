import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:admin@localhost:5432/test"
)

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
