#  vectors

def add(a, b):
    return [x + y for x, y in zip(a, b)]

def sub(a, b):
    return [x - y for x, y in zip(a, b)]

def magnitude(v):
    return sum(x ** 2 for x in v) ** 0.5

a = [1, 2, 3]
b = [4, 5, 6]
print(add(a, b))
print(sub(b, a))
print(magnitude(a))

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def cosine_similarity(a, b):
    return dot(a, b) / (magnitude(a) * magnitude(b))

a = [1, 2, 3]
b = [4, 5, 6]
print(dot(a, b))
print(cosine_similarity(a, b))

# Thursday: 29th october; 2026

# addition of vectors
def add(a: list, b: list):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

a = [6, 5, 4]
b = [3, 2, 1]
new = add(a, b)
print(new)

# subtraction of vectors
def sub(a: list, b: list):
    result = []
    for i in range(len(a)):
        result.append(a[i] - b[i])
    return result

a = [6, 5, 4]
b = [3, 2, 1]
new = sub(a, b)
print(new)
print(sub([1, 2, 3], [4, 5, 6]))
print(sub([4, 5, 6], [1, 2, 3]))

# vector magnitude
import math
def mag(a: list):
    result = 0
    for i in range(len(a)):
        square = a[i]**2
        result += square
    return math.sqrt(result)

print(mag([3, 4]))
print(mag([1, 2, 3]))

# dot product 
def dot(a: list, b: list):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

print(dot([1, 0], [0, 1]))
print(dot([2, 3], [4, 1]))
print(dot([1, 1], [-1, -1]))

"""
cosine similarity = dot product / (mag(a) * mag(b))

"""
def cosine_similarity(a: list, b: list):
    return dot(a, b) / (mag(a) * mag(b))

print(cosine_similarity([1, 1], [-1, -1]))
print(cosine_similarity([3, 4], [6, 8]))
print(cosine_similarity([2, 3], [4, 1]))


# matrix vector multiplication
def dot(a: list, b: list):
    if a == [] or b == []:
        return f"cannot use an empty list"

    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]

    return result

def matvec(m: list, v: list):
    result = []
    for i in range(len(m)):
        result.append(dot(m[i], v))

    return result

print(matvec([[2, 0], [0, 2]], [3, 4]))
print(matvec([[1, 2], [3, 4], [5, 6]], [10, 20]))

# Wednesday. 25th November; 2026
# 1. softmax, log-softmax, cross-entropy, and the lesson's exercises.

import math

def softmax(scores):
    biggest = max(scores)
    exps = []
    for s in scores:
        exps.append(math.exp(s - biggest))
    total = sum(exps)
    result = []
    for e in exps:
        result.append(e / total)
    return result

# Log-softmax

"""
From Step 6, training needs the log of each probability. Taking math.log(softmax(...)) can fail when a probability rounds to 0. So we compute it directly:
"""
# log_softmax(zᵢ) = zᵢ − log(Σ e^(zⱼ))
"""
The part log(Σ e^(zⱼ)) is called log-sum-exp, and we use the same "subtract the biggest" trick to keep it safe: log(Σ e^(zⱼ)) = biggest + log(Σ e^(zⱼ − biggest)).
"""
def log_softmax(scores):
    biggest = max(scores)
    total = 0
    for s in scores:
        total += math.exp(s - biggest)
    log_total = biggest + math.log(total)

    result = []
    for s in scores:
        result.append(s - log_total)
    return result

# Cross-entropy loss
"""
The loss is −(log probability of the correct class). target is the index of the correct class.
"""
def cross_entropy_loss(scores, target):
    return -log_softmax(scores)[target]

