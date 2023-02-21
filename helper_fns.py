def seq_along(list: list):
    return range(len(list))

def sort_dict(dictionary):
    sorted_d = dict(sorted(dictionary.items()))
    return sorted_d

def sample_skew(skew=4, mean=7, sd=15):
    skewed_dist = skewnorm(skew, mean, sd)
    skew_num = skewed_dist.rvs()
    skew_num_round = round(skew_num, 0)
    if skew_num_round < 1:
        return random.randint(1, 6)
    else: 
        return skew_num_round