def CheckWays(total_days):
    ways = []

    for i in range(total_days+1):
        ways.append(0)
    # print("ways: ", ways)

    ways[0], ways[1] = 1, 2


    for i in range(2, total_days + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
        if i >= 5:
            ways[i] -= ways[i - 5]

    
    return ways[total_days]

def ceremonyEligibility(total_days):
    no_of_ways = CheckWays(total_days)

    ways_without_missing = CheckWays(total_days - 1)

    probability_missing = no_of_ways - ways_without_missing

    return f"{no_of_ways}/{probability_missing}"



total_days = 5
print(ceremonyEligibility(total_days))



def countWays(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        if i >= 5:
            dp[i] -= dp[i - 5]

    return dp[n]

def probabilityMissCeremony(N):
    total_ways = countWays(N)
    ways_without_missing = countWays(N - 1)
    probability_missing = total_ways - ways_without_missing
    
    return f"{probability_missing}/{total_ways}"

# Test cases
# test_cases = [5, 10]
days = 5

# for days in test_cases:
result = probabilityMissCeremony(days)
print(f"For {days} days: {result}")
