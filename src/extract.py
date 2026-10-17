from pathlib import Path
import csv
from datetime import datetime
from collections import defaultdict

file_raw = Path("data/raw/AGL_001.TXT")
records = defaultdict(list)

with open(file_raw, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")

    for line in reader:
        date_text = line["DateTime"] 
        converted_date = datetime.strptime(date_text, "%Y/%m/%d %H:%M:%S")
        key = (line["EnNo"], converted_date.date())

        records[key].append(converted_date)

    for key, timestamped in records.items():
        ordered_times = sorted(timestamped)      
        print(f"Funcionario: {key[0]}")
        print(f"Data: {key[1]}")

        for timestamped in ordered_times:
            print(timestamped.time())
        print("-----------------------------------")




        