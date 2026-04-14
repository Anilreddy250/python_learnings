import subprocess
import json
import sys

def check_nvme_temparature(device="/dev/nvme0", threshold=70):
    try:
        #execute nvme-cli command to get smart-log in JSON format
        result = subprocess.run(
            ["sudo","nvme","smart-log", device, "-o","json"], capture_output=True, text=True,check=True
        )
        #parse the JSON output
        data = json.loads(result.stdout)
        #nvme temparature is typically reported in kelvin in raw logs.
        #but "nvme-cli" JSON output usually converts in to celsius for you
        #we strip the "c" or "k" if present and convert to integer
        temp_raw = data.get("temperature")
        if temp_raw is None:
            print(f"Error: Could not find temperature data for {device}")
            return
        #handle various output formats (some versios return '313 k' or 40c)
        # =
        if isinstance(temp_raw, str):
            current_temp = int(temp_raw.split()[0])
            #if the tool returned kelvin (over200), convert to celsius
            if "k" in temp_raw or current_temp > 200:
                current_temp -=273
        else:
            current_temp = temp_raw
        print(f"current temperature of {device}: {current_temp}C")
        #logi check
        if current_temp >= threshold:
            print(f"CRITICAL ERROR: Temperature reached {current_temp}°C!")
            #triggering a system exit with error code or calling an alert function
            sys.exit(1)
        else:
            print("Temperature is within safe liits")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run nvme-cli:{e}")
    except PermissionError:
        print(f"error: this script requires 'sudo' privileges to access Nvme logs")
    except Exception as e:
        print(f" an unexpected error occurred {e}")

if __name__ == "__main__":
    check_nvme_temparature(device="/dev/nvme0n1", threshold=70)



