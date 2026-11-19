import hashlib
import time
from werkzeug.security import generate_password_hash, check_password_hash

print("--- SHA-256（ソルトなし）---")
print(hashlib.sha256(b"guest").hexdigest())
print(hashlib.sha256(b"guest").hexdigest())

print("--- werkzeug（ソルトあり）---")
h1 = generate_password_hash("guest")
h2 = generate_password_hash("guest")
print(h1)
print(h2)

print("--- 照合 ---")
print(check_password_hash(h1, "guest"))
print(check_password_hash(h1, "guesu"))

print("--- 速さ比べ（100回）---")
start = time.time()
for _ in range(100):
    hashlib.sha256(b"guest").hexdigest()
print(f"SHA-256: {time.time() - start:.4f}秒")

start = time.time()
for _ in range(100):
    generate_password_hash("guest")
print(f"scrypt:  {time.time() - start:.4f}秒")