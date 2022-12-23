import csv
from datetime import datetime
# ['day', 'date', 'set', 'arm', 'position', 'duration', 'size', ]
data = [
    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "left",
        "position": "straight", "duration(sec)": 1.3, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "right",
        "position": "straight", "duration(sec)": 0.8, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "left",
        "position": "straight", "duration(sec)": 1.7, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "right",
        "position": "straight", "duration(sec)": 2.46, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "left",
        "position": "straight", "duration(sec)": 2.02, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "right",
        "position": "straight", "duration(sec)": 1.35, "size(mm)": 22},

    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "left",
        "position": "bent", "duration(sec)": 1.46, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "right",
        "position": "bent", "duration(sec)": 1.33, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "left",
        "position": "bent", "duration(sec)": 3.05, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "right",
        "position": "bent", "duration(sec)": 6.64, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "left",
        "position": "bent", "duration(sec)": 2.24, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "right",
        "position": "bent", "duration(sec)": 4.26, "size(mm)": 22},

    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "left",
        "position": "lockoff", "duration(sec)": 1.02, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "right",
        "position": "lockoff", "duration(sec)": 1.02, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "left",
        "position": "lockoff", "duration(sec)": 2.03, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "right",
        "position": "lockoff", "duration(sec)": 1.58, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "left",
        "position": "lockoff", "duration(sec)": 0.99, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "right",
        "position": "lockoff", "duration(sec)": 1.09, "size(mm)": 22}
]
with open("hangboard_data.csv", mode='w', newline="") as csvfile:
    feildnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=feildnames)
    writer.writerows(data)
