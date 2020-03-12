import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

dataframe = pd.read_csv("floatdata.csv")

x = dataframe.X

y = dataframe.Y

stats = linregress(x, y)

m = stats.slope

b = stats.intercept

# Change the default figure size​

plt.figure(figsize=(10,10))

# Change the default marker for the scatter from circles to x's​

plt.scatter(x, y, marker='x')

# Set the linewidth on the regression line to 3px​

plt.plot(x, m * x + b, color="red", linewidth=3)

# Add x and y lables, and set their font size​

plt.xlabel("Total payed $", fontsize=20)

plt.ylabel("Total traveled (Mi)", fontsize=20)

# Set the font size of the number lables on the axes​

plt.xticks(fontsize=18)

plt.yticks(fontsize=18)

plt.savefig("figure.png")