from pathlib import Path
import csv
from datetime import datetime
from collections import defaultdict


def load_data(file_raw):
    with open(file_raw, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter="\t")
        return list(reader)
def data_conversion(reader, records):
    for line in reader:
        date_text = line["DateTime"] 
        converted_date = datetime.strptime(date_text, "%Y/%m/%d %H:%M:%S")
        key = (line["EnNo"], converted_date.date())
        records[key].append(converted_date)
    return records

if __name__ == "__main__":
    file_raw = Path("data/raw/AGL_001.TXT")
    records = defaultdict(list)
    
    reader = load_data(file_raw)
    records = data_conversion(reader, records)








        