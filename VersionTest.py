import subprocess
from pathlib import Path

OtoPyVersion = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

OtoPyTags = (
    subprocess.run(["git", "tag"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
    .split()[-2]
    .split("v")[-1]
)
OtoPyTags
print(OtoPyVersion)
print(OtoPyTags)
assert "." in OtoPyTags

input("Click enter to close")