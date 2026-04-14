def is_leap(year):
    leap = False
    
    # Check if divisible by 400 (Always a leap year)
    if year % 400 == 0:
        leap = True
    # Check if divisible by 100 (Not a leap year)
    elif year % 100 == 0:
        leap = False
    # Check if divisible by 4 (Leap year)
    elif year % 4 == 0:
        leap = True
        
    return leap

year = int(input("Enter a year: "))
print(is_leap(year))