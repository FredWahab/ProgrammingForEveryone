def computepay(h, r):
    if hrs > 40 :
        ot = h - 40
        otRate = 1.5 * r
        return((40 * r) + (ot * otRate))
    else :
    	return(h * r)

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

p = computepay(hrs, rate)
print("Pay", p)
