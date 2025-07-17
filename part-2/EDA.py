import os  # to build file paths dynamically
import pandas as pd  # for data loading and manipulation
import matplotlib.pyplot as plt  # for creating visualizations

# Construct the full path to the CSV file based on this script's location
script_dir = os.path.dirname(__file__)  # get directory where EDA.py resides
csv_filename = "NANDURI Kushath Sri Krishna Rao - data.csv"  # data file name
csv_file = os.path.join(script_dir, csv_filename)  # full path to the CSV

# Load the CSV data into a DataFrame
df = pd.read_csv(csv_file)

# Convert 'Market value as of 31 December, 2023' from string to float
df["Market value as of 31 December, 2023"] = (
    df["Market value as of 31 December, 2023"]
    .str.replace(",", "")     # remove thousands separator commas
    .str.replace("$", "")     # remove dollar sign
    .astype(float)            # convert cleaned strings to numeric type
)

# Convert 'Number of shares' from string to float
df["Number of shares"] = (
    df["Number of shares"]
    .str.replace(",", "")     # remove commas
    .astype(float)            # convert to numeric
)

# Convert '% of total portfolio' from string to float
df["% of total portfolio"] = (
    df["% of total portfolio"]
    .str.replace("%", "")     # remove percent symbol
    .astype(float)            # convert to numeric
)

# Display DataFrame structure after cleaning
print("DataFrame info after cleaning:")
print(df.info())  # shows data types and non-null counts

# Display summary statistics for numeric columns
print("\nSummary statistics after cleaning:")
print(df.describe())  # basic stats: mean, std, min, max, etc.

# Identify numeric and categorical columns
num_cols = df.select_dtypes(include="number").columns  # list of numeric column names
cat_cols = df.select_dtypes(exclude="number").columns  # list of non-numeric column names

# --- Chart 1: Histogram of Market Value ---
plt.figure()  # start a new figure
plt.hist(df["Market value as of 31 December, 2023"])  # plot histogram bars
plt.title("Distribution of Market Value as of 31 Dec 2023")  # chart title
plt.xlabel("Market value (USD)")  # x-axis label
plt.ylabel("Number of companies")  # y-axis label
plt.show()  # render the plot

# --- Chart 2: Boxplot of Number of Shares ---
plt.figure()  # start another figure
plt.boxplot(df["Number of shares"])  # draw a boxplot
plt.title("Boxplot of Number of Shares")  # chart title
plt.ylabel("Number of shares")  # y-axis label
plt.show()  # render the plot

# --- Chart 3: Bar Chart of Domain Counts ---
plt.figure()  # start another figure
df["Domain"].value_counts().plot(kind="bar")  # bar chart of how many companies per domain
plt.title("Count of Companies by Domain")  # chart title
plt.xlabel("Domain")  # x-axis label
plt.ylabel("Count")  # y-axis label
plt.show()  # render the plot

# --- Chart 4: Scatter Plot of Shares vs. Market Value ---
plt.figure()  # start another figure
plt.scatter(
    df["Number of shares"],  # use number of shares for x-axis
    df["Market value as of 31 December, 2023"]  # use market value for y-axis
)  # plot scatter points
plt.title("Market Value vs. Number of Shares")  # chart title
plt.xlabel("Number of shares")  # x-axis label
plt.ylabel("Market value (USD)")  # y-axis label
plt.show()  # render the plot

# --- Chart 5: Correlation Matrix Heatmap ---
corr = df[num_cols].corr()  # compute correlation matrix among numeric columns
plt.figure()  # start another figure
plt.imshow(corr, interpolation="none")  # display matrix as image
plt.colorbar()  # add a color scale legend
plt.xticks(range(len(corr)), corr.columns, rotation=90)  # label x-axis ticks
plt.yticks(range(len(corr)), corr.index)  # label y-axis ticks
plt.title("Correlation Matrix of Numeric Features")  # chart title
plt.show()  # render the heatmap