"""Generate SECRET_KEY and JWT_SECRET_KEY for production."""
import secrets
print("SECRET_KEY=" + secrets.token_hex(32))
print("JWT_SECRET_KEY=" + secrets.token_hex(32))
