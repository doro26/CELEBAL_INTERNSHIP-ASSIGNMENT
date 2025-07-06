# This code is correct.
# It takes some numbers as input, stores them in a tuple, and prints the hash value of that tuple.
# The hash() function in Python can give both positive and negative numbers.
# So, if your output is negative, that's completely normal and still correct!
# The hash value can also change on different computers or Python versions.


--code


if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))