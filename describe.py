import pandas as pd
import numpy as np
import sys
from utils import load_csv, ft_mean, ft_std, ft_min, ft_percentile, ft_max


def ft_normalization(data: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize the data

    Args:
        data (pd.DataFrame): The dataset to normalize

    Returns:
        pd.DataFrame: The normalized dataset
    """
    normalized_data = data.copy()
    for column in data.columns:
        values = [x for x in data[column].values if not pd.isnull(x)]
        if all(isinstance(x, (int, float, np.int64, np.float64)) for x in values):
            min = ft_min(values)
            max = ft_max(values)
            normalized_data[column] = (normalized_data[column] - min) / (max - min)
        else:
            normalized_data[column] = data[column]
    return normalized_data


def ft_describe(data: pd.DataFrame) -> pd.DataFrame:
    """
    Create a DataFrame with the following statistics for each column:
    - Count: The number of non-null values
    - Mean: The mean of the values
    - Std: The standard deviation of the values
    - Min: The minimum value
    - 25%: The 25th percentile
    - 50%: The 50th percentile
    - 75%: The 75th percentile
    - Max: The maximum value
    - CV: The coefficient of variation (Std / Mean)
    - Std²: The variance (Std²)

    Args:
        data (pd.DataFrame): The dataset to describe

    Returns:
        pd.DataFrame: A DataFrame with the statistics for each column
    """
    statistics = {}
    for column in data.columns:
        values = [x for x in data[column].values if not pd.isnull(x)]
        if all(isinstance(x, (int, float, np.int64, np.float64)) for x in values):
            statistics[column] = {
                "Count": len(values),
                "Mean": ft_mean(values),
                "Std": ft_std(values),
                "Min": ft_min(values),
                "25%": ft_percentile(values, 25),
                "50%": ft_percentile(values, 50),
                "75%": ft_percentile(values, 75),
                "Max": ft_max(values),
                "CV": ft_std(values) / ft_mean(values),
                "Std²": ft_std(values) ** 2,
            }
    return pd.DataFrame(statistics)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python describe.py <file_path>")
        exit(1)
    data = load_csv(sys.argv[1])
    print("Original data:")
    print("")
    print(ft_describe(data))
    print("")
    print("Normalized data:")
    print("")
    print(ft_describe(ft_normalization(data)))
    # For comparison
    # print(data.describe())
