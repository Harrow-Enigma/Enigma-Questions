def digSum(n, s, level = 0):
    """
    A function that computes the number of n-digit numbers whose digit sums are s.

    This is a recursive function, helping speed up the computation
    by orders of magnitude when compared to a simple for-loop.

    A 'level' of 0 denotes that this is the first time this function
    has been called, i.e. it has not entered any recursive loops yet.
    """

    # If the sum is larger than 9 times the no. of digits or the sum is less than 0,
    # then no n-digit number can exist which has a digit sum of s. 0 is therefore returned.
    # When the recurrent function hits this condition, it stops calling on itself.
    if (s > 9*n or s < 0):
        return 0
    
    # With invalid sums now ruled out, if n is a one-digit number, then there can only
    # be one possible digit whose sum equals the required digit sum.
    # This is the other terminating condition for this recursive function.
    elif n == 1:
        return 1
    

    # When the digit sum is valid and the number of digits is not 0, we essentially
    # loop through all the possible first digits less than or equal to sum, and add
    # up the number of possible n-1 digit numbers whose digit sums equal the original
    # sum (s) minus the chosen first digit number, by recursively calling this function.

    # E.g. Find number of 2-digit numbers whose digit sums are 3.
    # | Loop   i: Choose first digit as 1 --> no. of 1 digit numbers with digit sum 2 is 1. |
    # | Loop  ii: Choose first digit as 2 --> no. of 1 digit numbers with digit sum 1 is 1. |
    # | Loop iii: Choose first digit as 3 --> no. of 1 digit numbers with digit sum 0 is 1. |
    # | Loop  iv: Choose first digit as 4 --> bigger than sum, loop terminates              |
    # | Add up results --> 1 + 1 + 1 = 3                                          |
    # ---------------------------------------------------------------------------------------
    # Therefore there are 3 2-digit numbers who digit sums are 3.
    # ---------------------------------------------------------------------------------------
    # See? This program doesn't have to loop through all 2-digit numbers to find the ans.

    # This has the advantage of only looping through viable digits, so throughout the
    # whole algorithm, mostly everything looped through is viable, making it efficient.
    else:
        r = 0   # This variable holds the total number of n-digit numbers

        # A n-digit number does not start with 0, so if 
        if level != 0:
            r += digSum(n-1, s, 1)
    
        for i in range(1, 10):
            if i <= s:
                r += digSum(n-1, s-i, 1)
            else:
                break
        
        return r


n = int(input('Enter n: '))
d = int(input('Enter d: '))

# If d is 1, then all n-digit numbers are divisible by it.
if d == 1:
    p = 9 * (10 ** (n-1))

# if d is not one, then we loop through the possible multiples of d and sum up the possible
# n-digit numbers whose digit sum equals these multiples
else:
    p = 0
    for m in range(1, (9*n)//d + 1):
        p += digSum(n, m*d)

print(p)
print(p)

"""
========================================== Marking ==========================================
These test inputs will be carried out on your program, and should all run in under 6 seconds.
Each checked box [*] represents 1 successful run, and hence 1 mark.

Test inputs:

[*]     n = 3       d = 7       out: 126
[*]     n = 2       d = 79      out: 0
[*]     n = 2       d = 5       out: 18
[*]     n = 6       d = 10      out: 90000                  [0 X 4]
[*]     n = 7       d = 10      out: 900000                 [0 X 5]
[*]     n = 7       d = 60      out: 84
[*]     n = 6       d = 54      out: 1
[*]     n = 20      d = 176     out: 8855
[*]     n = 15      d = 133     out: 120
[*]     n = 17      d = 145     out: 735471
[*]     n = 13      d = 105     out: 2702609
[*]     n = 20      d = 1       out: 90000000000000000000   [0 x 19]

    Total: [12]/[12]

Merry Christmas,
Team Enigma
"""
