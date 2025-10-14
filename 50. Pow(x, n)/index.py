def myPow(x: float, n: int) -> float:
    def power(x, n):
        if n == 0:
            return 1
        half = power(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    if n < 0:
        x = 1 / x
        n = -n
    return power(x, n)

print("Example 1:")
print("Input: x = 2.00000, n = 10")
print("Output:", round(myPow(2.00000, 10), 5))

print("\nExample 2:")
print("Input: x = 2.10000, n = 3")
print("Output:", round(myPow(2.10000, 3), 5))

print("\nExample 3:")
print("Input: x = 2.00000, n = -2")
print("Output:", round(myPow(2.00000, -2), 5))