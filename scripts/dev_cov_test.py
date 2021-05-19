import subprocess
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
subprocess.run(
    ["coverage", "run", "manage.py", "test", "--settings=woice.settings.testing"],
    cwd=root_dir,
)
subprocess.run(["coverage", "report"], cwd=root_dir)
subprocess.run(["coverage", "html"], cwd=root_dir)
