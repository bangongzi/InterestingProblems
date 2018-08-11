from math import factorial

def perm(n, m):
    return factorial(n) / factorial(n - m)

def comb(n, m):
    return perm(n, m) / factorial(m)

def volumn(n, m):
    # 返回在n个‘a’、m个‘z’前提下，字典中有多少个单词
    return comb(n + m, n)

def find_k(n, m, k, path):
    if n == 0 or m == 0:
        if k == 1:
            return path + n * 'a' + m * 'z'
        else:
            return -1
    if volumn(n - 1, m) < k:
        res = find_k(n, m - 1, k - volumn(n -1, m), path + 'z')
    elif volumn(n - 1, m) == k:
        res = path + n * 'a' + m * 'z'
        res = path + 'a' + m * 'z' + (n - 1) * 'a'
    else:
        res = find_k(n - 1, m, k, path + 'a')
    return res

# Test
n, m= 2, 2
for k in range(1, 8):
    print(find_k(n, m, k, ''))
