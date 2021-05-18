import subprocess
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent

subprocess.run(
    ["python", "manage.py", "makemigrations", "--settings=woice.settings.develop"],
    cwd=root_dir,
)
