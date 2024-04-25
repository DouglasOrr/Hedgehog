import subprocess
import sys

base_names = [line.split("==")[0] for line in sys.stdin]

cmd = ["pip", "install", "--upgrade", *base_names]
print(f"$ {cmd}", file=sys.stderr)
subprocess.check_call(cmd)

new_names = subprocess.check_output(["pip", "freeze"]).decode().split("\n")
for line in new_names:
    if line.split("==")[0] in base_names:
        print(line)
