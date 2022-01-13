#validates input
try :
	score = float(input("Enter Score: "))
except:
    score = -1

#assigns score to valid input or returns error
if score <= 1 and score >= 0 :
    if score >= 0.9 :
        print('A')
    elif score >= 0.8 :
        print('B')
    elif score >= 0.7 :
        print('C')
    elif score >= 0.6 :
        print('D')
    else :
        print('F')
else :
    print('Invalid Score Entry')
    exit()
