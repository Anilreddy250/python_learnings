#given a list of pcie error codes, return a dictionary containing the count error, but onpy for errors that occured more than once.
# def filter_error_counts(errors):
#     counts = {}
#     for error in errors:
#         counts[error] = counts.get(error, 0)+1
#     return {k :v  for k ,v in counts.items() if v>1}
# error_log = ["0x10", "0x20", "0x10", "0x40", "0x20", "0x10"]
# print(filter_error_counts(error_log))

# memory efficient data processing qn: you need to process a massive file containing sensor data(millions of lines) how do you read and print lines containing the word "CRITICAL" without crashing the system's memory?
# def stream_critical_errors(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             if "CRITICAL" in line:
#                 yield line.strip()

# # Execution logic
# log_file = "/home/mirafra/Desktop/python_learnings/data.txt"

# print("Streaming Critical Errors:")
# for error in stream_critical_errors(log_file):
#     print(f"Found: {error}")
# # file_path = "/home/mirafra/Desktop/python_learnings/data.txt"
#string manipulation the anagram check: qns: write a function to check if two strings are anagrams of each other eg(silent, listen)?

# def is_Anagram(str1, str2):
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()

#     if len(str1) != len(str2):
#         print("is not a anagram")
#     return sorted(str1) == sorted(str2)
# print(is_Anagram("adkdck", "Dam"))

# 4 Hardware register parsing(bonus): given an integer representing a 32 bit register, write a function to check if the 3rd bit(index2) is set to 1.
# def check_third_bit(register_value):
#     mask = 1<<2
#     return (register_value & mask) !=0
# print(check_third_bit(8))

# mask = 1<<2 #value is 4 (binary 0100)
# status = 14 #binary 0111
# #check if the 3rd bit is set using the bitwise AND (&)
# if status & mask:
#     print("The third bit is active!!")

# finding the missing number qns: you have an array containing all integers from 1 to n , except one is missing how do you find the missing number ?
# def find_missing_number(arr,n):
#     expected_sum = n*(n+1)//2
#     actual_sum = sum(arr)
#     return expected_sum - actual_sum
# nums = [1,2,3,5,6,7,8,9]
# print(find_missing_number(nums, 9))
#reverse a linked list: given the head of a singly link list reverse the list and return the new head?

# class listNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def reverse_linked_list(head):
#     prev = None
#     current = head
#     while current:
#         next_node = current.next # store the next node
#         current.next  = prev
#         prev = current
#         current = next_node
#     return prev
# # node3 = listNode(6)
# # node2 = listNode(5, node3)
# node1 = listNode(4)#, node2)

# ans = reverse_linked_list(node1)
# while ans:
#     print(ans.val, end=" -> " if ans.next else "")
#     ans = ans.next

#the args and kwargs mystery: what are the *args and **kwargs, and why would you use them ?
# *args: allows a function to accept any number of positional arguments(passed as a tuple).
# **kwargs allow for any number of keyword arguments (passed as a dictionary).
# def log_hardware_Status(component, *flags, **details):
#     print(f"component: {component}")
#     print(f"active flags:{flags}")
#     print(f"Device specs: {details}")
# log_hardware_Status("GPU","overclocked","highTemp",manufacturer = "Nvidia", memory = "16gb")

#decorator(The Timer) Write a decorator that prints the execution time of a function.?
import time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
@timer_decorator
def process_Data():
    time.sleep(6) #simulating a delay
process_Data()
