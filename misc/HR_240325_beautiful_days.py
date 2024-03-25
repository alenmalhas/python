def beautifulDays(i, j, k):
    beautiful_days_list = [x for x in range(i, j+1) if is_beautiful(x, k)]
    return len(beautiful_days_list)
    
def is_beautiful(num, k):
    numRev = int(str(num)[::-1])
    diff = abs(numRev-num)
    isBeautiful = diff % k == 0
    return isBeautiful

