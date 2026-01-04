import statistics

def column_stats(sheet, col):
    # Make an array of all the actual number values in the column, then calculate mean, median, and mode with built in library functions.
    values = [row[col] for row in sheet.data if isinstance(row[col], (int, float))]
    return {
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "mode": statistics.mode(values)
    }
