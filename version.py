import subprocess
from pathlib import Path

OtoPyVersion = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in OtoPyVersion

VFile = str(Path(__file__)).replace(f"{Path(__file__).stem}.py","OtoPy/VERSION")
with open(VFile,"w") as file:
    file.write(OtoPyVersion)