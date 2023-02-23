import numpy as np
import random
from scipy.stats import skewnorm

def seq_along(list: list):
    return range(len(list))

def norm_array(array):
    range = (np.max(array) - np.min(array))
    norm_arr = (array - np.min(array))/max(range, 0.0001)
    return norm_arr

def sample_skew(skew=5, mean=2, sd=15, size=1) -> int:
    """Sample integer(s) from customer item distribution

    Args:
        skew (int, optional): _description_. Defaults to 5.
        mean (int, optional): _description_. Defaults to 2.
        sd (int, optional): _description_. Defaults to 15.
        size (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    # Create distribution
    skewed_dist = skewnorm(skew, mean, sd)
    # Sample from distribution
    skew_num = skewed_dist.rvs(size)
    # Replace negative numbers (and 0) with low positive values 
    strictly_pos = np.where(skew_num < 1, random.randint(1, 10), skew_num)
    # Return integer
    return int(strictly_pos)