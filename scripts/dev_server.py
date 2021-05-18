import subprocess
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
subprocess.run(
    [
        "python",
        "manage.py",
        "runserver",
        "0.0.0.0:8016",
        "--settings=woice.settings.develop",
    ],
    cwd=root_dir,
)
