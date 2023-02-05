# ['day', 'date', 'set', 'arm (1=left,2=right)', 'position(straight=1,bent=2,lockoff=3)', 'duration', 'size', ]
data = [
    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "1",
        "position": "1", "duration(sec)": 1.3, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "2",
        "position": "1", "duration(sec)": 0.8, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "1",
        "position": "1", "duration(sec)": 1.7, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "2",
        "position": "1", "duration(sec)": 2.46, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "1",
        "position": "1", "duration(sec)": 2.02, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "2",
        "position": "1", "duration(sec)": 1.35, "size(mm)": 22},

    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "1",
        "position": "2", "duration(sec)": 1.46, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "2",
        "position": "2", "duration(sec)": 1.33, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "1",
        "position": "2", "duration(sec)": 3.05, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "2",
        "position": "2", "duration(sec)": 6.64, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "1",
        "position": "2", "duration(sec)": 2.24, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "2",
        "position": "2", "duration(sec)": 4.26, "size(mm)": 22},

    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "1",
        "position": "3", "duration(sec)": 1.02, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 1, "arm": "2",
        "position": "3", "duration(sec)": 1.02, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "1",
        "position": "3", "duration(sec)": 2.03, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 2, "arm": "2",
        "position": "3", "duration(sec)": 1.58, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "1",
        "position": "3", "duration(sec)": 0.99, "size(mm)": 22},
    {"day": 1, "date": "2022-12-23", "set": 3, "arm": "2",
        "position": "3", "duration(sec)": 1.09, "size(mm)": 22},

    {"day": 2, "date": "2022-12-26", "set": 1, "arm": "1",
        "position": "1", "duration(sec)": 1.8, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 1, "arm": "2",
        "position": "1", "duration(sec)": 2.34, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 2, "arm": "1",
        "position": "1", "duration(sec)": 1.98, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 2, "arm": "2",
        "position": "1", "duration(sec)": 1.57, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 3, "arm": "1",
        "position": "1", "duration(sec)": 1.59, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 3, "arm": "2",
        "position": "1", "duration(sec)": 3.23, "size(mm)": 22},

    {"day": 2, "date": "2022-12-26", "set": 1, "arm": "1",
        "position": "2", "duration(sec)": 2.32, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 1, "arm": "2",
        "position": "2", "duration(sec)": 3.76, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 2, "arm": "1",
        "position": "2", "duration(sec)": 2.04, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 2, "arm": "2",
        "position": "2", "duration(sec)": 4.02, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 3, "arm": "1",
        "position": "2", "duration(sec)": 4.28, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 3, "arm": "2",
        "position": "2", "duration(sec)": 7.35, "size(mm)": 22},

    {"day": 2, "date": "2022-12-26", "set": 1, "arm": "1",
        "position": "3", "duration(sec)": 1.82, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 1, "arm": "2",
        "position": "3", "duration(sec)": 1.65, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 2, "arm": "1",
        "position": "3", "duration(sec)": 2.51, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 2, "arm": "2",
        "position": "3", "duration(sec)": 3.63, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 3, "arm": "1",
        "position": "3", "duration(sec)": 2.09, "size(mm)": 22},
    {"day": 2, "date": "2022-12-26", "set": 3, "arm": "2",
        "position": "3", "duration(sec)": 2.71, "size(mm)": 22},

    {"day": 3, "date": "2022-12-29", "set": 1, "arm": "1",
        "position": "1", "duration(sec)": 2.25, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 1, "arm": "2",
        "position": "1", "duration(sec)": 3.19, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 2, "arm": "1",
        "position": "1", "duration(sec)": 1.81, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 2, "arm": "2",
        "position": "1", "duration(sec)": 4.58, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 3, "arm": "1",
        "position": "1", "duration(sec)": 1.72, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 3, "arm": "2",
        "position": "1", "duration(sec)": 5.72, "size(mm)": 22},

    {"day": 3, "date": "2022-12-29", "set": 1, "arm": "1",
        "position": "2", "duration(sec)": 3.00, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 1, "arm": "2",
        "position": "2", "duration(sec)": 3.73, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 2, "arm": "1",
        "position": "2", "duration(sec)": 2.83, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 2, "arm": "2",
        "position": "2", "duration(sec)": 3.77, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 3, "arm": "1",
        "position": "2", "duration(sec)": 2.82, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 3, "arm": "2",
        "position": "2", "duration(sec)": 5.5, "size(mm)": 22},

    {"day": 3, "date": "2022-12-29", "set": 1, "arm": "1",
        "position": "3", "duration(sec)": 1.9, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 1, "arm": "2",
        "position": "3", "duration(sec)": 3.43, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 2, "arm": "1",
        "position": "3", "duration(sec)": 2.06, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 2, "arm": "2",
        "position": "3", "duration(sec)": 2.87, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 3, "arm": "1",
        "position": "3", "duration(sec)": 1.78, "size(mm)": 22},
    {"day": 3, "date": "2022-12-29", "set": 3, "arm": "2",
        "position": "3", "duration(sec)": 3.97, "size(mm)": 22},

    {"day": 4, "date": "2023-02-01", "set": 1, "arm": "1",
        "position": "1", "duration(sec)": 1.74, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 1, "arm": "2",
        "position": "1", "duration(sec)": 3.08, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 2, "arm": "1",
        "position": "1", "duration(sec)": 3.87, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 2, "arm": "2",
        "position": "1", "duration(sec)": 5.2, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 3, "arm": "1",
        "position": "1", "duration(sec)": 3.58, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 3, "arm": "2",
        "position": "1", "duration(sec)": 5.53, "size(mm)": 22},

    {"day": 4, "date": "2023-02-01", "set": 1, "arm": "1",
        "position": "2", "duration(sec)": 4.19, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 1, "arm": "2",
        "position": "2", "duration(sec)": 7.46, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 2, "arm": "1",
        "position": "2", "duration(sec)": 3.62, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 2, "arm": "2",
        "position": "2", "duration(sec)": 5.64, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 3, "arm": "1",
        "position": "2", "duration(sec)": 3.48, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 3, "arm": "2",
        "position": "2", "duration(sec)": 6.41, "size(mm)": 22},

    {"day": 4, "date": "2023-02-01", "set": 1, "arm": "1",
        "position": "3", "duration(sec)": 1.87, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 1, "arm": "2",
        "position": "3", "duration(sec)": 3.85, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 2, "arm": "1",
        "position": "3", "duration(sec)": 2.02, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 2, "arm": "2",
        "position": "3", "duration(sec)": 3.94, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 3, "arm": "1",
        "position": "3", "duration(sec)": 1.25, "size(mm)": 22},
    {"day": 4, "date": "2023-02-01", "set": 3, "arm": "2",
        "position": "3", "duration(sec)": 3.18, "size(mm)": 22},


    {"day": 5, "date": "2023-02-05", "set": 1, "arm": "1",
     "position": "1", "duration(sec)": 1.6, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 1, "arm": "2",
        "position": "1", "duration(sec)": 5.22, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 2, "arm": "1",
        "position": "1", "duration(sec)": 2.76, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 2, "arm": "2",
        "position": "1", "duration(sec)": 5.91, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 3, "arm": "1",
        "position": "1", "duration(sec)": 2.47, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 3, "arm": "2",
        "position": "1", "duration(sec)": 4.49, "size(mm)": 22},

    {"day": 5, "date": "2023-02-05", "set": 1, "arm": "1",
        "position": "2", "duration(sec)": 5.25, "size(mm)": 22},
    {"day": 5, "date": "2023-01-05", "set": 1, "arm": "2",
        "position": "2", "duration(sec)": 6.84, "size(mm)": 22},
    {"day": 5, "date": "2023-01-05", "set": 2, "arm": "1",
        "position": "2", "duration(sec)": 3.56, "size(mm)": 22},
    {"day": 5, "date": "2023-01-05", "set": 2, "arm": "2",
        "position": "2", "duration(sec)": 6.64, "size(mm)": 22},
    {"day": 5, "date": "2023-01-05", "set": 3, "arm": "1",
        "position": "2", "duration(sec)": 3.91, "size(mm)": 22},
    {"day": 5, "date": "2023-01-05", "set": 3, "arm": "2",
        "position": "2", "duration(sec)": 5.0, "size(mm)": 22},

    {"day": 5, "date": "2023-02-05", "set": 1, "arm": "1",
        "position": "3", "duration(sec)": 2.5, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 1, "arm": "2",
        "position": "3", "duration(sec)": 4.55, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 2, "arm": "1",
        "position": "3", "duration(sec)": 1.65, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 2, "arm": "2",
        "position": "3", "duration(sec)": 2.27, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 3, "arm": "1",
        "position": "3", "duration(sec)": 1.74, "size(mm)": 22},
    {"day": 5, "date": "2023-02-05", "set": 3, "arm": "2",
        "position": "3", "duration(sec)": 3.83, "size(mm)": 22}

]
