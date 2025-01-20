import random

def play_roulette(number):
    # get result from roll
    roll = random.randint(1, 38)
    result = []
    # check results
    is_0 = "P0"
    is_00 = "P00"
    is_red_or_odd = "PR PO"
    is_black_or_even = "PB PE"
    is_low = "P1-18"
    is_high = "P19-38"

    if roll == 37:
        result.append(is_0)
    elif roll == 38:
        result.append(is_00)
    if roll != 37 or 38:
        if roll % 2 == 0:
            result.append(is_black_or_even)
        else:
            result.append(is_red_or_odd)
    if roll in range(1, 18):
        result.append(is_low)
    if roll in range(19, 36):
        result.append(is_high)
    
    
    bet = "P"+str(number).zfill(2)
    if bet == "P37":
        bet = "P0"
    if bet == "P38":
        bet = "P0"
    print(bet)
    print(result)
    
play_roulette(38)