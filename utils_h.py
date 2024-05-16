import pandas as pd
import numpy as np

def myMax(column):
    max = float('-inf')
    for n in range(len(column)):
        if max < column[n]:
            max = column[n]
    return max

def myMin(column):
    min = float('inf')
    for n in range(len(column)):
        if min > column[n]:
            min = column[n]
    return min

def myCount(column):
    myCount = 0
    for n in range(len(column)):
        if not pd.isnull(column[n]):
            myCount += 1
    return myCount

def myMean(column):
    sum = 0
    for n in range(len(column)):
        if not np.isnan(column[n]).all():
            sum += column[n]
    return sum / myCount(column)

def myStd(column):
    sum_square = 0
    column_mean = myMean(column)

    for n in (column):
        if not pd.isnull(n):
            sum_square += (n - column_mean) ** 2
    return (sum_square / (myCount(column) - 1)) ** 0.5

def median_of_three(column):
    if len(column) < 3:
        return column[0] if isinstance(column, list) else column.iloc[0]
    first = column[0] if isinstance(column, list) else column.iloc[0]
    middle = column[len(column) // 2] if isinstance(column, list) else column.iloc[len(column) // 2]
    last = column[-1] if isinstance(column, list) else column.iloc[-1]

    if (first - middle) * (last - first ) >= 0:
        return first
    if (middle - first) * (last - middle) >= 0:
        return middle
    else:
        return last

def myQuickSort(column):

    if len(column) <= 1:
        return column
    pivot = median_of_three(column)
    less = [x for x in column if x < pivot]
    equal = [x for x in column if x == pivot]
    greater = [x for x in column if x > pivot]
    return myQuickSort(less) + equal + myQuickSort(greater)


def myDropNan(column):
    new_column = []
    for n in range(len(column)):
        if not pd.isnull(column[n]):
            new_column.append(column[n])
    return new_column

def myQuartile(column):
    column = myDropNan(column)
    column = myQuickSort(column)
    n = len(column)

    def find_median(sorted_list):
        mid = len(sorted_list) // 2
        if len(sorted_list) % 2 == 0:
            return (sorted_list[mid - 1] + sorted_list[mid]) / 2
        else:
            return sorted_list[mid]

    q1 = find_median(column[:n // 2])
    q2 = find_median(column)
    q3 = find_median(column[-(n // 2):])

    return q1, q2, q3


def replaceNanWithMean(df):
    for column in df.columns:
        mean = myMean(df[column])
        for i in range(len(df[column])):
            if pd.isnull(df.loc[i, column]):
                df.loc[i, column] = mean 
                
    return df

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