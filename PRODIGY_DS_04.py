import pandas as pd

# Read the CSV file
df = pd.read_csv('twitter_validation.csv')

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())
# Re-load the dataset by adding the 'header' parameter set to None
df = pd.read_csv('twitter_validation.csv', header = None)

# Rename the columns
df.columns = ['ID', 'Topic', 'Sentiment', 'Tweet']

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())
import altair as alt

# Get unique values in `Sentiment` column
unique_sentiments = df['Sentiment'].unique()

# Print the unique values in the `Sentiment` column
print(f"Unique values in 'Sentiment' column: {unique_sentiments}")

# Count the occurrences of each sentiment
sentiment_counts_df = df['Sentiment'].value_counts().reset_index()
sentiment_counts_df.columns = ['Sentiment', 'Count']

# Print the sentiment counts
print(sentiment_counts_df.to_markdown(index=False, numalign="left", stralign="left"))

# Create a bar chart for sentiment distribution
bar_chart = alt.Chart(sentiment_counts_df).mark_bar().encode(
    x=alt.X('Sentiment', axis=alt.Axis(title='Sentiment')),
    y=alt.Y('Count', axis=alt.Axis(title='Number of Tweets')),
    tooltip=['Sentiment', 'Count']
).properties(
    title='Sentiment Distribution in Social Media Data'
)

# Save the chart as a JSON file
bar_chart.save('sentiment_distribution.json')
