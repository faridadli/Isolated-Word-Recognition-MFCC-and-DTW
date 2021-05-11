import numpy as np

def noise_gating(time_series, threshold):
    series = np.array([])
    for i in range(time_series.size):
        if time_series[i] >= threshold[0] and time_series[i] <= threshold[1]:
            series = np.append(series, 0)
        else:
            series = np.append(series, time_series[i])
    return series

def zero_align(time_series):
    series = np.array([])
    for i in range(time_series.size):
        if time_series[i] != 0:
            series = time_series[i + 1:]
            break
    return series