allName, biggerName = "Sonita,Jonh,Michel,Bora,Seyha,VannaPiseth", ""
arrayName = allName.split(",")
for name in arrayName : 
    if (len(name)) >= 5 : 
        biggerName += (name + "\n")
print(biggerName)