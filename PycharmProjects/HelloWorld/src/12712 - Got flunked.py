max_in = 1000000000000000000
max_odd_in = 499999999999999999

def binary_search(l, r, x, two):
    while l <= r:
        mid = l + (r - 1) // 2
        print(mid)
        odd_mid = 2 * mid + 1
        result = (odd_mid * (odd_mid - 1)) // 2 + (two - 1) * odd_mid
        # Check if x is present at mid
        if result == x:
            return mid

            # If x is greater, ignore left half
        elif result < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

T = int(input())
for i in range(T):
    n = int(input())
    ans = max_in+1
    two = 1
    for j in range(60):
        k = binary_search(0, max_odd_in, n, two)
        if k != -1:
            odd_k = (2*k+1)*two
            if ans > odd_k:
                ans = odd_k
        two = two * 2
    if ans == max_in+1:
        ans = -1
    print(ans)
