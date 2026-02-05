# Write your solution here
def factorials(n: int):
    d = {}
    value = 1
    for key in range(1,n+1):
        value = 1
        for i in range(1,key+1):
            value *= i

        d[key] = value
    return d

if __name__ == "__main__":
    print(factorials(n))

### model solution ###
def factorials(n: int):
    result = {}
    result[1] = 1  # here,below logic doesn't apply (1!) != 0
    for i in range(2, n + 1):
        result[i] = result[i-1] * i  # n! = n * (n-1)!
    return result
# Write your solution here