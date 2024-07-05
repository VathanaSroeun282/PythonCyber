#!/usr/bin/python
# -*- coding: <UTF-8> -*-

class DOG:
    def __init__(self, dogID, dogName, dogSex, dogStatus):
        self.dogID = dogID
        self.dogName = dogName
        self.dogSex = dogSex
        self.dogStatus = dogStatus
        
    def dogInfo(self):
        dogInfoText = ""
        dogInfoText += f"Dog's ID     : {str(self.dogID)}\n"
        dogInfoText += f"Dog's Name   : {self.dogName}\n"
        dogInfoText += f"Dog's Sex    : {self.dogSex}\n"
        dogInfoText += f"Dog's Status : {self.dogStatus}\n"
        return dogInfoText

class MyDog(DOG):
    def __init__(self, checkDogID, dID, dName, dSex, dStatus):
        super().__init__(dID, dName, dSex, dStatus)
        self.checkDogID = checkDogID

    def CheckInfoMyDog(self):
        if self.dogID == self.checkDogID:
            print(self.dogInfo())
        else:
            print("Your Dog is not available!")

AllDog1 = MyDog(1, 1, "Kiki", "Male", "alive")
AllDog1.CheckInfoMyDog()