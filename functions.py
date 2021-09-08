def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            # if the year is divisible by 4 and by 100 and by 400
            if year % 400 == 0:
                leap = True
            # if the year is divisible by 4 and by 100 but not by 400
            elif year % 400 != 0:
                leap = False
        # if year is divisible by 4 but not by 100
        elif year % 100 != 0:
            leap = True
        
    return leap

year = int(input())
print(is_leap(year))