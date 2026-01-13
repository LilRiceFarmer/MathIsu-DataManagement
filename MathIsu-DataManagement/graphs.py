import matplotlib.pyplot as plt
import numpy as np

def scatter_with_correlation(sheet, x, y):
    xs, ys = [], []

    # Extract only numeric (x, y) pairs
    for row in sheet.data:
        try:
            xs.append(float(row[x]))
            ys.append(float(row[y]))
        except (ValueError, TypeError):
            continue

    if len(xs) < 2:
        print("Not enough numeric data to plot correlation.")
        return

    xs = np.array(xs)
    ys = np.array(ys)

    m, b = np.polyfit(xs, ys, 1)
    corr = np.corrcoef(xs, ys)[0, 1]

    # Correlation description
    if corr > 0.7:
        t = "Strong Positive"
    elif corr > 0.3:
        t = "Weak Positive"
    elif corr < -0.7:
        t = "Strong Negative"
    elif corr < -0.3:
        t = "Weak Negative"
    else:
        t = "No correlation"

    plt.scatter(xs, ys)
    plt.plot(xs, m * xs + b)
    plt.title(f"Correlation: {corr:.2f} ({t})")
    plt.xlabel(sheet.headers[x])
    plt.ylabel(sheet.headers[y])
    plt.show()


def box_plot_column(sheet, col):
    values = []

    # Collect only numeric values
    for row in sheet.data:
        try:
            values.append(float(row[col]))
        except (ValueError, TypeError):
            continue

    if len(values) < 2:
        print("Not enough numeric data to create a box plot.")
        return

    plt.boxplot(values)
    plt.title(f"Box Plot of {sheet.headers[col]}")
    plt.ylabel(sheet.headers[col])
    plt.show()
