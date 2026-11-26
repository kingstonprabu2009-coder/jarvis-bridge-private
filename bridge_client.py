import json, time, urllib.request, subprocess

URL = "https://raw.githubusercontent.com/kingstonprabu2009-coder/jarvis-bridge-private/main/tasks/queue.json"
PROJECT = "/data/data/com.termux/files/home/opendroid"
seen = ""

print("JARVIS BRIDGE CONNECTING...")

while True:
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": "JARVIS"})
        with urllib.request.urlopen(req, timeout=15) as r:
            task = json.loads(r.read())

        tid = task.get("task_id", "")
        if tid and tid != seen:
            print("\nTASK:", task)
            if task.get("action") == "git_status":
                if input("Approve? (yes/no): ").lower() == "yes":
                    p = subprocess.run(
                        ["git", "-C", PROJECT, "status", "--short", "--branch"],
                        capture_output=True, text=True
                    )
                    print(p.stdout or p.stderr)
            else:
                print("Unsupported action; not executed.")
            seen = tid

        time.sleep(15)
    except KeyboardInterrupt:
        print("Bridge stopped.")
        break
    except Exception as e:
        print("Connection:", e)
        time.sleep(15)
