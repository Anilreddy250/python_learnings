# import subprocess

# def run_executable(command):
#     try:
#         # capture_output grabs the result so you can print it in python
#         result = subprocess.run(command, capture_output=True, text=True, shell=True)
#         print("Output:", result.stdout)
#         if result.stderr:
#             print("Errors:", result.stderr)
            
#     except Exception as e:
#         print(f"Failed to run executable: {e}")

# # Example: run a command (change command as needed)
# run_executable("ls")

# subprocess.run("sudo reboot", shell = True)

import subprocess
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)  # See the output
print(result.returncode)  # See the exit code