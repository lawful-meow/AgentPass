import hashlib
import os
from pathlib import Path

EXCLUDE_DIRS = {'.git', 'node_modules', 'dist', 'build', 'agentpass_checkpoints', '__pycache__', '.venv', 'venv'}
EXCLUDE_EXTS = {'.rsp3', '.lock', '.log'}

def compute_integrity_hash(directory='.'):
    hasher = hashlib.sha256()
    root_path = Path(directory).resolve()
    
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        dirs.sort()
        files.sort()
        
        for file in files:
            if any(file.endswith(ext) for ext in EXCLUDE_EXTS):
                continue
            filepath = Path(root) / file
            rel_path = filepath.relative_to(root_path)
            hasher.update(str(rel_path).encode('utf-8'))
            hasher.update(b'\0')
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    hasher.update(chunk)
    return hasher.hexdigest()

if __name__ == "__main__":
    print(f"Project Integrity Hash: {compute_integrity_hash()}")
