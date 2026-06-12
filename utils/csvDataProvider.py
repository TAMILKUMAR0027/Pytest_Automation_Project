import csv
import os


class CsvDataProvider:

    @staticmethod
    def get_data(csv_path, scenario_key):
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"[CSV ERROR] CSV file not found: {csv_path}")

        rows = []
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("scenario") == scenario_key:
                    rows.append(row)
        return rows

    @staticmethod
    def get_first_row(csv_path, scenario_key):
        rows = CsvDataProvider.get_data(csv_path, scenario_key)
        return rows[0] if rows else None