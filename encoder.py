import os
import base64

CHUNK_SIZE = 1024 * 1024  # 1 MB chunks
INPUT_FILE = 'miniconda.zip'
OUTPUT_DIR = 'miniconda_chunks'

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_FILE, 'rb') as f:
    i = 0
    while chunk := f.read(CHUNK_SIZE):
        b64_chunk = base64.b64encode(chunk).decode('ascii')
        with open(os.path.join(OUTPUT_DIR, f'chunk_{i:04d}.txt'), 'w', encoding='utf-8') as out:
            out.write(b64_chunk)
        i += 1

print(f'Done! {i} chunks created in "{OUTPUT_DIR}"')
