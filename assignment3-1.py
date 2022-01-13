hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate per Hour:"))

if hrs > 40 :
    ot = hrs - 40
    otRate = 1.5 * rate
    print((40 * rate) + (ot * otRate))
else :
    print(hrs * rate)
