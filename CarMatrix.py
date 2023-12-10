import pandas as pd

def generate_car_matrix(df):
    # Pivot the DataFrame based on the specified rules
    result_df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    
    # Set diagonal values to 0
    result_df.values[[range(len(result_df))]*2] = 0
    
    return result_df

# Assuming you have loaded the dataset-1.csv into a DataFrame named 'df'
# Example usage:
# df = pd.read_csv('dataset-1.csv')
# result_matrix = generate_car_matrix(df)
