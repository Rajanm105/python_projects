from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hash):
    return pwd_context.verify(password, hash)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
