import csv
import os


class CsvDataProvider:

    def get_csv_data(file_path):
        with open(file_path, mode="r", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    
    def get_csv_data_by_test_name(file_path, test_name):
        rows = CsvDataProvider.get_csv_data(file_path)
        return [row for row in rows if row["test_name"] == test_name]