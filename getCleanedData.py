import pandas as pd

# Read the train.csv file
df = pd.read_csv('./train.csv')

# Filter the Body column where the Tags column contains "java"
filtered_df = df[df['Tags'].str.contains('java|python')][['Tags', 'Body']]

#I want to delete all the tags from the Tags column that are not exactly "java" or "python"
filtered_df['Tags'] = filtered_df['Tags'].apply(lambda x: 'java' if 'java' in x else 'python' if 'python' in x else '')

# Save the filtered_df to a CSV file
filtered_df.to_csv('/home/matteoforni/Documents/SUPSI/3anno/nlp/NLPStackOverflow/filtered_data.csv', index=False)
# Print the filtered Body column
print(filtered_df)