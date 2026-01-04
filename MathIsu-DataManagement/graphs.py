import matplotlib.pyplot as plt
import numpy as np

def scatter_with_correlation(sheet, x, y):
    xs, ys = [], []

    # filters through to find the number value eg getting rid of N/A, strings etc..
    for row in sheet.data:
        try:
            x_val = float(row[x])
            y_val = float(row[y])
            xs.append(x_val)    
            ys.append(y_val)
        except (ValueError, TypeError):
            continue  

    # Convert lists to numpy arrays for easier math operations
    xs = np.array(xs)
    ys = np.array(ys)

    # Make sure we have at least 2 numbers to calculate correlation
    if len(xs) < 2:
        print("Not enough numeric data to plot correlation.")
        return
    
    # Fit a line to the points (y = m*x + b) and calculate correlation coefficient
    m, b = np.polyfit(xs, ys, 1)
    corr = np.corrcoef(xs, ys)[0, 1]

    # Decide what type of correlation it is
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

    plt.scatter(xs, ys) # Plot the points
    plt.plot(xs, m * xs + b, color="red")    # Plot the best-fit line in red
    plt.title(f"Correlation: {corr:.2f} ({t})")
    plt.xlabel(sheet.headers[x])    # Add title and labels
    plt.ylabel(sheet.headers[y])    # Add title and labels
    plt.show()
