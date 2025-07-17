# i havent used ai to write the code and i have reused parts of code from the homework 

import os  # I need os to build a path to my data file automatically
import pandas as pd  # pandas helps me load and work with the CSV
import matplotlib.pyplot as plt  # matplotlib lets me create charts

# Figure out where this script is so I can load the CSV from the same folder
script_dir = os.path.dirname(__file__)  # gets the directory of EDA.py
csv_filename = "NANDURI Kushath Sri Krishna Rao - data.csv"  # name of my data file
csv_file = os.path.join(script_dir, csv_filename)  # full path to the CSV

# Read the data into a DataFrame so I can explore it
df = pd.read_csv(csv_file)

# Clean up the market value column by removing commas and $ then convert to float
df["Market value as of 31 December, 2023"] = (
    df["Market value as of 31 December, 2023"]
    .str.replace(",", "")  # strip out commas
    .str.replace("$", "")  # strip out the dollar sign
    .astype(float)         # convert text to numeric
)

# Clean up the number of shares column: drop commas and convert to float
df["Number of shares"] = (
    df["Number of shares"]
    .str.replace(",", "")  # remove commas for thousands
    .astype(float)         # convert to numeric
)

# Clean up the portfolio percentage: remove % sign and convert to float
df["% of total portfolio"] = (
    df["% of total portfolio"]
    .str.replace("%", "")  # drop percent symbol
    .astype(float)         # convert to numeric
)

# Print info so I can see column types and check for missing data
print("DataFrame info after cleaning:")
print(df.info())

# Print summary statistics to get an overview of the numeric columns
print("\nSummary statistics after cleaning:")
print(df.describe())

# Identify which columns are numeric versus categorical
num_cols = df.select_dtypes(include="number").columns  # numeric columns
cat_cols = df.select_dtypes(exclude="number").columns  # non-numeric columns

# Chart 1: Histogram of Market Value
plt.figure()  # start a new chart
plt.hist(df["Market value as of 31 December, 2023"])  # plot histogram
plt.title("Distribution of Market Value as of 31 Dec 2023")  # add title
plt.xlabel("Market value (USD)")  # label x-axis
plt.ylabel("Number of companies")  # label y-axis
plt.show()  # display the chart

# Chart 2: Boxplot of Number of Shares
plt.figure()  # open a new chart
plt.boxplot(df["Number of shares"])  # draw boxplot
plt.title("Boxplot of Number of Shares")  # add title
plt.ylabel("Number of shares")  # label y-axis
plt.show()  # show the boxplot

# Chart 3: Bar Chart of Domain Counts
plt.figure()  # open another chart
df["Domain"].value_counts().plot(kind="bar")  # bar chart of domain counts
plt.title("Count of Companies by Domain")  # add title
plt.xlabel("Domain")  # label x-axis
plt.ylabel("Count")  # label y-axis
plt.show()  # show the bar chart

# Chart 4: Scatter Plot of Shares vs. Market Value
plt.figure()  # open a new chart
plt.scatter(
    df["Number of shares"],  # x-axis data
    df["Market value as of 31 December, 2023"]  # y-axis data
)  # plot scatter points
plt.title("Market Value vs. Number of Shares")  # add title
plt.xlabel("Number of shares")  # label x-axis
plt.ylabel("Market value (USD)")  # label y-axis
plt.show()  # display the scatter plot

# Chart 5: Correlation Matrix Heatmap 
corr = df[num_cols].corr()  # calculate correlations among numeric columns
plt.figure()  # open a new chart
plt.imshow(corr, interpolation="none")  # display correlation matrix
plt.colorbar()  # show color scale legend
plt.xticks(range(len(corr)), corr.columns, rotation=90)  # label x-axis ticks
plt.yticks(range(len(corr)), corr.index)  # label y-axis ticks
plt.title("Correlation Matrix of Numeric Features")  # add title
plt.show()  # display the heatmap