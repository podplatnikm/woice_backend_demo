import subprocess
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent
subprocess.run(
    ["docker", "exec", "-it", "woice_web", "/bin/bash"], cwd=root_dir, shell=True
)
