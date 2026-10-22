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