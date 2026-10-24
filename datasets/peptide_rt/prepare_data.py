"""Recreate the attributed classroom sample from its fixed public source."""
import gzip
import hashlib
import io
import json
from pathlib import Path
from urllib.request import urlopen

import pandas as pd

folder = Path(__file__).resolve().parent
metadata = json.loads((folder / "provenance.json").read_text())
source = urlopen(metadata["url"], timeout=60).read()
assert hashlib.sha256(source).hexdigest() == metadata["sha256"], "Unexpected source contents"
raw = pd.read_csv(io.BytesIO(source))
assert len(raw) == metadata["source_rows"] and raw["sequence"].is_unique
assert raw["sequence"].str.fullmatch("[ACDEFGHIKLMNPQRSTVWY]+").all()
assert not raw.isna().any().any()
data = raw.sample(n=metadata["snapshot_rows"], random_state=42).reset_index(drop=True)
with gzip.GzipFile(filename=str(folder / "peptides_6000.csv.gz"), mode="wb", mtime=0) as output:
    output.write(data.to_csv(index=False).encode())
print("Prepared", len(data), "peptides with their supplied iRT targets.")
