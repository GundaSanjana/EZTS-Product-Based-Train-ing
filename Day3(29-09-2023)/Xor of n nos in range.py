'''Find XOR for all the numbers for the given range.
given a range l-r/print xor
lets say
l=2 r=5
2^3^4^5

l=2 r=4
2^3^4 ans:5
dont use loop,get O(1)
lets say 4 to 9
xor(4 to 9)^xor(1 to 3)
(1^2^3^4^5^6^7^8^9)^(1^2^3)
in above 1 2 3 xors will get cancelled
generalize xor(r)^xor(l-1)'''


def xor_range(l, r):
    # Function to calculate XOR of numbers from 1 to N
    def xor_up_to_n(N):
        if N % 4 == 0:
            return N
        elif N % 4 == 1:
            return 1
        elif N % 4 == 2:
            return N + 1
        else:
            return 0

    # Calculate XOR for the given range
    xor_result = xor_up_to_n(r) ^ xor_up_to_n(l - 1)

    return xor_result

# Test cases
#result1 = xor_range(2, 5)
result2 = xor_range(int(input()), int(input()))

print(result2)
