from scipy.stats import pearsonr
from scipy.stats import kendalltau

a = [15,12,8, 8, 7, 7, 7, 6, 5, 3]
b = [10,25,17,11,13,17,20,13,9, 15]

pearson_corr, _ = pearsonr(a, b)
kendall_corr, _ = kendalltau(a, b)

result = pearson_corr

print(f'{result:.3f}')