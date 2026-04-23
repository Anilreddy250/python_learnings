import csv

def update_salaries(input_file, output_file):
    updated_data = []
    fieldnames = None # Initialize as None
    
    try:
        with open(input_file, mode='r') as file:
            reader = csv.DictReader(file)
            
            # Read the rows first
            for row in reader:
                if row['department'] == 'Sales':
                    # Calculate 10% increase
                    new_salary = int(row['salary']) * 1.1
                    row['salary'] = str(int(new_salary))
                updated_data.append(row)
            
            # Capture fieldnames AFTER reading or by accessing property
            fieldnames = reader.fieldnames

        if not fieldnames:
            print("Error: The input CSV file is empty or has no headers.")
            return

        with open(output_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_data)
            
        print(f"Success! Updated salaries saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file at {input_file} was not found.")
    except KeyError as e:
        print(f"Error: Column {e} not found in CSV. Check your header names.")

# Execute
update_salaries(
    "/home/mirafra/Desktop/python_learnings/practice_prep/csv/csv.csv", 
    "/home/mirafra/Desktop/python_learnings/practice_prep/csv/upadated_csv.csv"
)