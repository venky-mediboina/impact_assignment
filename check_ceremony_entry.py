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

    return f"{probability_missing}/{no_of_ways}"



total_days = 5
print(ceremonyEligibility(total_days))
