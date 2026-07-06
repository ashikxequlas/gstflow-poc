import json
import csv
import os


class Storage:

    def __init__(self):

        self.output_folder = "../outputs"

        os.makedirs(self.output_folder, exist_ok=True)

    def save_json(self, invoices):

        with open(
            os.path.join(self.output_folder, "extracted_invoices.json"),
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(invoices, file, indent=4)

        print("JSON Saved")

    def save_csv(self, invoices):

        if len(invoices) == 0:
            return

        with open(
            os.path.join(self.output_folder, "extracted_invoices.csv"),
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=invoices[0].keys()
            )

            writer.writeheader()

            writer.writerows(invoices)

        print("CSV Saved")