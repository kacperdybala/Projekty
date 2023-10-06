# Enter

# name = input('Whats is your name? ').title()
# print('Hello,', name)

# Zodiac sign 
def validation():
    day = int(input('Provide day of your birth in number format '))
    if not (1<=day<=31):
        print("wrong day")
        return 0
    month = int(input('Provide month of your birth in number format '))
    if not (1<=month<=12):
        print("wrong month") 
        return 0

    if((21<=day and month==3) or (day<=19 and month==4) ):
        print("Your zodiac sign is ram")
    if((20<=day and month==4) or (day<=20 and month==5) ):
        print("Your zodiac sign is bull")
    if((21<=day and month==5) or (day<=20 and month==6) ):
        print("Your zodiac sign is twins")
    if((23<=day and month==6) or (day<=22 and month==7) ):
        print("Your zodiac sign is cancer")
    if((23<=day and month==7) or (day<=22 and month==8) ):
        print("Your zodiac sign is lion")
    if((23<=day and month==8) or (day<=22 and month==9) ):
        print("Your zodiac sign is woman")
    if((23<=day and month==9) or (day<=22 and month==10) ):
        print("Your zodiac sign is wage")
    if((23<=day and month==10) or (day<=21 and month==11) ):
        print("Your zodiac sign is scoprio")
    if((22<=day and month==11) or (day<=21 and month==12) ):
        print("Your zodiac sign is shooter")
    if((22<=day and month==12) or (day<=19 and month==1) ):
        print("Your zodiac sign is capricorn")
    if((20<=day and month==1) or (day<=18 and month==2) ):
        print("Your zodiac sign is aquaman")
    if((19<=day and month==2) or (day<=20 and month==3) ):
        print("Your zodiac sign is fish")

validation() 