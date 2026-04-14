import subprocess
import re

results = subprocess.run("ls", capture_output=True, shell=True)
print (results)
# def check_pcie_link(bdf_address):
#     try:
#         # Run lspci -vvv for the specific BDF address
#         result = subprocess.check_output(
#             ["lspci", "-s", bdf_address, "-vvv"], 
#             stderr=subprocess.STDOUT, 
#             universal_newlines=True
#         )

#         # Regex to find Speed and Width in LnkCap and LnkSta
#         # LnkCap: Port #0, Speed 16GT/s, Width x4 ...
#         # LnkSta: Speed 8GT/s, Width x4 ...
#         cap_match = re.search(r"LnkCap:.*Speed (\d+GT/s), Width (x\d+)", result)
#         sta_match = re.search(r"LnkSta:.*Speed (\d+GT/s), Width (x\d+)", result)

#         if cap_match and sta_match:
#             max_speed, max_width = cap_match.groups()
#             cur_speed, cur_width = sta_match.groups()

#             print(f"Device {bdf_address} Report:")
#             print(f"Capabilities: {max_speed} {max_width}")
#             print(f"Current Status: {cur_speed} {cur_width}")

#             if max_speed != cur_speed:
#                 print("WARNING: Link speed is downgraded!")
#             elif max_width != cur_width:
#                 print("WARNING: Link width is downgraded!")
#             else:
#                 print("SUCCESS: Link is running at optimal performance.")
#         else:
#             print("Could not parse PCIe Link information.")

#     except subprocess.CalledProcessError as e:
#         print(f"Error running lspci: {e}")

# if __name__ == "__main__":
#     import sys

#     if len(sys.argv) != 2:
#         print("Usage: python pcie/prep.py <BDF address>")
#         print("Example: python pcie/prep.py 01:00.0")
#     else:
#         check_pcie_link(sys.argv[1])