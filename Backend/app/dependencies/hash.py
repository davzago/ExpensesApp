from passlib.context import CryptContext

hash_context = CryptContext(schemes=["sha256_crypt"])
