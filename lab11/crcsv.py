import csv

# Data to write to the CSV file
data = [
    {"name": "Yeras", "surname": "bab", "phone": "345"}
]

# CSV file path
csv_file = "contact.csv"

# Field names
fieldnames = ["name", "surname", "phone"]

# Writing data to the CSV file
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="\t")
    
    # Write header
    writer.writeheader()
    
    # Write data
    for row in data:
        writer.writerow(row)

print("CSV file created successfully!")

