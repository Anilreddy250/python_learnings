# we use the built-in sys module. sys.argv is a list where the first element is the script name itself

# import sys

# def main():
#     #check is arguments were passed (sys.argv[0] is the script name)
#     if len(sys.argv)>1:
#         print(f"TOtal arguments received: {len(sys.argv)-1}")
#         for i, arg in enumerate(sys.argv[1:],1):
#             print(f"Argument {i}: {arg}")
#     else:
#         print("No arguments provided. Usage: python script.py arg1 arg2")
# if __name__ == "__main__":
#     main()

import sys

# Check command-line arguments
if len(sys.argv) < 2:
    print("Usage: script.py <argument>")
    # sys.exit(1)
print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")