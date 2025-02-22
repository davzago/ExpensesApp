from passlib.context import CryptContext

hash_context = CryptContext(schemes=["sha256_crypt"])

def hash_password(password: str):
    return hash_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return hash_context.verify(password, hashed_password)
