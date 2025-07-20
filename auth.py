from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import HTTPException, Depends
from passlib.context import CryptContext
from config import SECRET_KEY, ALGORITHM
from sqlalchemy.orm import session
from jose import jwt, JWTError
from fastapi import APIRouter
from database import get_db

auth_router = APIRouter(prefix='/auth')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def verify_token(token: str):

    try:
        user = jwt.decode(token, SECRET_KEY, ALGORITHM)
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail={'message': 'User has been denied access', 'reason': 'User is unauthorized'})

@auth_router.post('/signup')
async def user_registration(user: str, db: session = Depends(get_db)):
    pass