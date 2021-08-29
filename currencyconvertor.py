with open("data.txt")as f:
    lines= f.readlines()
currencydict = {}
for line in lines:
    part=line.split("\t")
    currencydict[part[0]]=part[1]
#print(currencydict)
amount=int(input("enter the amount you want to convert"))
print("select the name of currency you want to convert this amount to?\n Available options are")
print(currencydict.keys())

currency =input("please enter the name of currency from above\n ")
amountnew=0
amountnew=amount*float(currencydict[currency])
print(f"{amount} INR is equal to {amountnew} {currency}")