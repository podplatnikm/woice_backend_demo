import subprocess
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent.parent
subprocess.run(["docker", "compose", "up", "-d"], cwd=root_dir)
