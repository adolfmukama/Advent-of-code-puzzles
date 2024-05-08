fh = open("/home/kali/Documents/puzzles/puz01.txt", "r")
lines = fh.readlines()
total1 = 0
total2 = 0

for line in lines:
    var = []
    for i in line:
        if i.isdigit():
            var.append(i)
            
    if len(var) < 1:
        continue
    elif len(var) < 2:
        digit = int("".join([var[0], var[len(var)-1]]))
        total1 += digit
        
    else:
        new_list = int("".join([var[0], var[len(var)-1]]))
        total2 += int("".join([var[0], var[len(var)-1]]))
        
total = total1 + total2
print (f"The number of calibration \nvalues is {total}")
