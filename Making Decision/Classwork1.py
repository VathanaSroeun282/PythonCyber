# temp_c, temp_f = eval(input("Enter the temperature of celsius : ")), eval(input("Enter the temperature of fahrenheit : "))
temp = "45F,102C"
idTemp = temp.split(',')
result1, result2 = "", "";

if 'F' in idTemp[0]:
    C = (5/9) * (int(idTemp[0].replace("F", "")) - 32)
    result1 = f"{C:.2f}C"
elif 'C' in idTemp[0]:
    F = (int(idTemp[0].replace("C", ""))*(9/5)) + 32
    result1 = f"{F:.2f}F"

#tem2
if 'F' in idTemp[1]:
    C = (5/9) * (int(idTemp[1].replace("F", "")) - 32)
    result2 = f"{C:.2f}C"
elif 'C' in idTemp[1]:
    F = (int(idTemp[1].replace("C", ""))*(9/5)) + 32
    result2 = f"{F:.2f}F"

print("Conver of fahrenheit = "+ idTemp[0] +" is : " + result1 + "\nConver of celsius = "+ idTemp[1] +" is : " + result2)