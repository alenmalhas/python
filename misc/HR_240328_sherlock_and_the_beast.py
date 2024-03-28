def find_divisible_num(l:int):
    while l > 0:
        if l % 5 == 0:
            return l
        elif l % 3 ==0:
            return l
        l -= 5

    return -1


def decentNumber(l:int):
    #possible = ((l % 5) % 3) == 0
    divisible_num = find_divisible_num(l)
    if divisible_num == -1:
        return -1
    
    remainder = l - divisible_num
    division = (int) (divisible_num / 3)
    print(f"l: {l}, reminder: {remainder}, divisible_num: {divisible_num}, division: {division}")
    
    outStr = "5"*remainder + "3"*divisible_num
    print(outStr)

    return outStr

def sherlockBeastNaive(N):
    if (N < 3): 
        return "-1" 
    
    three_cnt = (int)(N//3)
    five_cnt = 0 

    while three_cnt >=0:
        rem = N - three_cnt*3
        if rem % 5 == 0:
            five_cnt = (int)(rem/5)
            break
        three_cnt -= 1
        
    if three_cnt <= 0 and five_cnt == 0:
        return "-1"
    
    return "555"*three_cnt + "33333"*five_cnt

def sherlockBeast(N):
    K = 5*((2*N)%3)
    if K > N:
        return -1
    else:
        return '5' * (N-K) + '3'*K