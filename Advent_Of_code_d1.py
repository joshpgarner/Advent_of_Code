import fileinput

ElvesTotal = []

single_cals = 0
run = 0
top4 = 0
for line in fileinput.input(files="/Users/josh9188/ac1.txt"):
    line = line.rstrip()
    if line == "":
        ElvesTotal.append(single_cals)
        single_cals = 0
    else:
        single_cals += int(line)


ElvesTotal.append(single_cals)

ElvesTotal.sort(reverse=True)


for item in ElvesTotal:
    top4 += item
    run += 1
    if run == 3:
        break


print (top4)


