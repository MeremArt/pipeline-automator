import csv
from io import StringIO

def parse_csv(file_content):
    reader = csv.DictReader(StringIO(file_content))
    return list(reader)

def get_column_names(rows):
    return list(rows[0].keys()) if rows else []
