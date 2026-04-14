import csv 
def log_attendance():
    roll_no = input("Enter Roll no:")
    name = input("Enter a nmae")
    student_class = input("enter class")
    #define the data row
    data = [roll_no, name, student_class]
    #open the file in appedn mode (a)
    #newline ='' prevents extra blank lines on some systems
    with open('./csv.csv', mode= 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print(f"attendance logged{name}")

# if __name__ =="__main__":
log_attendance()

