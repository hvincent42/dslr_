import pandas as pd
from utils import load_csv

def compare(data1: pd.DataFrame, data2: pd.DataFrame) -> None:
    """
    Compare two DataFrames

    Args:
        data1 (pd.DataFrame): The first DataFrame
        data2 (pd.DataFrame): The second DataFrame

    Returns:
        float: The percentage of similarity between the two DataFrames
    """
    col1 = data1.columns[1]
    col2 = data2.columns[1]

    if len(data1) != len(data2):
        print("The two DataFrames have different lengths")
        return

    error = 0

    for i in range(len(data1)):
        if data1[col1][i] != data2[col2][i]:
            print(f"Row {i} is different: {data1[col1][i]} != {data2[col2][i]}")
            error += 1

    print(f"Percentage of similarity: {1 - error / len(data1) * 100}%")



if __name__ == "__main__":
    data1 = load_csv("data1.csv")
    data2 = load_csv("data2.csv")
    compare(data1, data2)