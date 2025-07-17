# Import the wbdata package and Python’s datetime module
import wbdata
import datetime

# Use wbdata to get Chile’s total population from 2010 through 2020
data = wbdata.get_data(
    indicator='SP.POP.TOTL',       # World Bank code for total population
    country='CHL',                  # ISO code for Chile
    date=(                          # Date range tuple: start and end
        datetime.datetime(2010, 1, 1),
        datetime.datetime(2020, 12, 31),
    )
)

# Loop over each entry in the returned data list
for entry in data:
    # Pull out country name, year, and the population value
    country = entry['country']['value']
    year = entry['date']
    population = entry['value']
    # Print in a neat “Country – Year: Population” format with commas
    print(f"Country: {country}, Year: {year}, Population: {population:,}")