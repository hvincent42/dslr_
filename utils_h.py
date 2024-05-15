import pandas as pd

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
        if not pd.isnull(column[n]):
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
            if pd.isnull(df[column].iloc[i]):
                df[column].iloc[i] = mean
    return df