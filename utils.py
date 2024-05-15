import os
import pandas as pd
import math


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the CSV data.
    """
    try:
        if not isinstance(file_path, str):
            raise TypeError("The path must be a string.")
        if not file_path:
            raise ValueError("The path must not be empty.")
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)
        if not file_path.lower().endswith(".csv"):
            raise AssertionError("The file must be a CSV file.")

        data = pd.read_csv(file_path)

        # print("Loading dataset of dimensions " + str(data.shape))

        if data is None:
            raise AssertionError("Failed to load CSV.")

        return data

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


def ft_mean(values: list) -> float:
    """
    Calculate the mean of a list of values.

    Args:
        values (list): The list of values to calculate the mean of.

    Returns:
        float: The mean of the values.
    """
    try:
        return sum(values) / len(values)
    except Exception:
        return float("NaN")


def ft_std(values: list) -> float:
    """
    Calculate the standard deviation of a list of values.

    Args:
        values (list): The list of values to calculate the standard deviation of.

    Returns:
        float: The standard deviation of the values.
    """
    try:
        mean = ft_mean(values)
        n = len(values)
        return math.sqrt(sum((x - mean) ** 2 for x in values) / n)
    except Exception:
        return float("NaN")


def ft_percentile(values: list, percentile: float) -> float:
    """
    Calculate the percentile of a list of values.

    Args:
        values (list): The list of values to calculate the percentile of.
        percentile (float): The percentile to calculate (0-100).

    Returns:
        float: The percentile of the values.
    """
    try:
        values.sort()
        index = (len(values) - 1) * percentile / 100
        lower = values[int(index)]
        upper = values[int(index) + 1]
        return lower + (upper - lower) * (index - int(index))
    except Exception:
        return float("NaN")


def ft_min(values: list) -> float:
    """
    Calculate the minimum value of a list of values.

    Args:
        values (list): The list of values to calculate the minimum of.

    Returns:
        float: The minimum value of the values.
    """
    try:
        min_value = values[0]
        for value in values:
            if value < min_value:
                min_value = value
        return min_value
    except Exception:
        return float("NaN")


def ft_max(values: list) -> float:
    """
    Calculate the maximum value of a list of values.

    Args:
        values (list): The list of values to calculate the maximum of.

    Returns:
        float: The maximum value of the values.
    """
    try:
        max_value = values[0]
        for value in values:
            if value > max_value:
                max_value = value
        return max_value
    except Exception:
        return float("NaN")