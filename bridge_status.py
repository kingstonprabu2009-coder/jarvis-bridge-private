import os
import json
import subprocess
from datetime import datetime, timezone

ROOT = os.path.expanduser("~/opendroid")
print("JARVIS TERMUX BRIDGE")
print("Time:", datetime.now(timezone.utc).isoformat())
print("Project exists:", os.path.isdir(ROOT))

if os.path.isdir(ROOT):
    def run(args):
        return subprocess.run(
            args, cwd=ROOT, text=True,
            capture_output=True, timeout=15
        )

    branch = run(["git", "branch", "--show-current"])
    status = run(["git", "status", "--short", "--branch"])

    print("Branch:", branch.stdout.strip() or branch.stderr.strip())
    print("Git status:")
    print(status.stdout.strip() or status.stderr.strip())

print("Bridge client: READY")
print("GitHub relay: NOT CONNECTED")
