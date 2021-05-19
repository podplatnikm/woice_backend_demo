import subprocess
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent

subprocess.run(
    ["pytest"],
    cwd=root_dir,
)
# subprocess.run(
#     [
#         "python",
#         "manage.py",
#         "test",
#         "accounts.tests.UserTestCase",
#         "--settings=woice.settings.testing",
#     ],
#     cwd=root_dir,
# )
# subprocess.run(
#     [
#         "python",
#         "manage.py",
#         "test",
#         "chat.tests.LobbyTestCase",
#         "--settings=woice.settings.testing",
#     ],
#     cwd=root_dir,
# )
