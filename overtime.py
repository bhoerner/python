#simple overtime calculation
sh = input("Enter Hours: ")
sr = input("Enter Rates: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:",xp)
