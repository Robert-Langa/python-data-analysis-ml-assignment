import pandas as pd
import calendar
import webbrowser

# Load CSV and strip whitespace
df = pd.read_csv('q7-crosstab-data.csv')
df.columns = df.columns.str.strip()

# Convert numeric month to 3-letter abbreviation
df['month'] = df['month'].apply(lambda x: calendar.month_abbr[int(x)])

# Month order
month_order = list(calendar.month_abbr)[1:]  # ['Jan', 'Feb', ..., 'Dec']

# Crosstab 1: Months by Duration
months_by_duration = pd.crosstab(df['month'], df['duration'])
months_by_duration = months_by_duration.reindex([m for m in month_order if m in months_by_duration.index])

# Crosstab 2: Year by Month
year_by_month = pd.crosstab(df['year'], df['month'])
existing_months = [m for m in month_order if m in year_by_month.columns]
year_by_month = year_by_month[existing_months]

# Print minimal output
print("Months by Duration:")
print(months_by_duration)
print("\nYear by Month:")
print(year_by_month)

# Create HTML
html_content = f"""
<html>
<head>
    <title>Crosstab Summaries</title>
</head>
<body>
    <h2>Months by Duration</h2>
    {months_by_duration.to_html()}

    <h2>Year by Month</h2>
    {year_by_month.to_html()}
</body>
</html>
"""

# Write HTML file
html_file = "q7-crosstab-summaries.html"
with open(html_file, "w") as f:
    f.write(html_content)

# Optional: open in browser
webbrowser.open(html_file)
