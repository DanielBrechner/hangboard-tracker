import csv
import pandas as pd
from data import data

with open("hangboard_data.csv", mode='w', newline="") as csvfile:
    feildnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=feildnames)
    writer.writeheader()
    writer.writerows(data)
