# 6-mashq
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

primes_1_30 = tuple(i for i in range(1, 31) if is_prime(i))
print("6)", primes_1_30)

# 7-mashq
sample_nums = [-5, 0, 3, 12, -1, 9]
positives = tuple(x for x in sample_nums if x > 0)
print("7)", positives)

# 8-mashq
pairs_num_square = tuple((i, i*i) for i in range(1, 16))
print("8)", pairs_num_square)

# 9-mashq
sample_text = "salom dunyo bugun qanday"
last_chars = tuple(word[-1] for word in sample_text.split())
print("9)", last_chars)

# 10-mashq
nums_1_20 = list(range(1, 21))
squares_at_odd_indices = tuple(nums_1_20[i]**2 for i in range(len(nums_1_20)) if i % 2 == 1)
print("10)", squares_at_odd_indices)
