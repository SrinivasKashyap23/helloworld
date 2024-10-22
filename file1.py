import pandas as pd
dataset = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\PROJECT SCHOOL\archive\fitness_tracker_dataset.csv')
print(dataset.head(20))
dataset.fillna(dataset.mean(), inplace=True)
input_data = dataset[['steps', 'distance_km', 'workout_type']]
print("Helloworld")



