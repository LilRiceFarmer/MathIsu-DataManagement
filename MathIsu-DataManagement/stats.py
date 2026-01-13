import statistics
import numpy as np

def column_stats(sheet, col):
    # Collect only numeric values from the column
    values = [row[col] for row in sheet.data if isinstance(row[col], (int, float))]

    if len(values) == 0:
        raise Exception("No numeric data in this column.")

    return {
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "mode": statistics.mode(values)
    }


def column_box_stats(sheet, col):
    # Collect only numeric values (ignore text, blanks, etc.)
    values = [row[col] for row in sheet.data if isinstance(row[col], (int, float))]

    if len(values) < 2:
        raise Exception("Not enough numeric data for box plot statistics.")

    values.sort()

    q1 = np.percentile(values, 25)
    q3 = np.percentile(values, 75)

    return {
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "mode": statistics.mode(values),
        "Q1": q1,
        "Q3": q3,
        "IQR": q3 - q1
    }
