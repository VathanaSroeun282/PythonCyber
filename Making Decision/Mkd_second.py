userInfo = "001,Vathana,Male,Phnom Penh"
userArray = userInfo.split(",");
userID, userName = eval(input("Input your ID : ")), input("Input your user name : ")
if (userID == userArray[0]) & (userName == userArray[1]) : 
    for info in userArray : 
        print(info + "\n")
else :
    if userID != userArray[0]:
        print("Wrong user id!")
    elif userName != userArray[1]: 
        print("Wrong user name!")
