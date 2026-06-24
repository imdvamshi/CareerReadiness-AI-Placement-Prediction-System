import pandas as pd

def load_data():
    data = pd.read_csv("../Data/placement_dataset_2026.csv")
    return data