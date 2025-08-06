import csv
import json

csv_file_path = "data/NYC.csv"
json_file_path = "broad.json"

data_dict = {}

try:
    with open(csv_file_path, 'r') as file:
        lines = file.readlines()

        for line in lines[1:]: 
            geography, percent_obese = line.strip().split(',')
            percent_obese = float(percent_obese)  

            data_dict[geography] = percent_obese


    with open(json_file_path, "w") as json_file:
        json.dump(data_dict, json_file, indent=4)
    print(f"JSON file '{json_file_path}' created successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
