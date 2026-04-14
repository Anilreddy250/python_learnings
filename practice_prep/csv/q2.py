import csv
def count_records(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None) # skip the header row
            #count the remaining rows
            count = sum(1 for row in reader)
            print(f"total number of records:{count}")
    except FileNotFoundError:
        print(f"error the file{filename}was not found")

if __name__ == "__main__":
    count_records("attendance.csv")