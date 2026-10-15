import hashlib
from pathlib import Path

def sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def verify_digest(actual_digest: str, trusted_digest: str) -> bool:
    return bool(trusted_digest) and actual_digest.lower() == trusted_digest.lower()
