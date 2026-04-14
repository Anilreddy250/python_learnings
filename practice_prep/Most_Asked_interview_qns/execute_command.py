# import subprocess
# command = "ls -ltr"
# result = subprocess.run(command, shell=True, capture_output=True, text=True)
# print("Output:\n",result.stdout)
# if result.stderr:
#     print("Error:\n", result.stderr)

#secure way to run external commands without shell=false
# import subprocess
# command = ["ls", "-ltr"]

# result = subprocess.run(command, capture_output=True, text=True)
# print(result.stdout)

#in automation, you usually want the script to stop if the linux command fails, you can add check= True

import subprocess
# from sys import stdout
try :
    subprocess.run("sudo reboot", shell=True, check=True, capture_output=True, text=True)
    print("Command executed successfully")
except subprocess.CalledProcessError as e:
    print(f"command failed with exit code {e.returncode}")
    print(f"Error message:{e.stderr}")


