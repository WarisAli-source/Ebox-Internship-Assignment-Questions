from Stall import Stall
name=input("Enter the name of the stall:\n")
det=input("Enter the detail of the stall:\n")
on=input("Enter the owner name of the stall:\n")
StallType=input("Enter the type of the stall:\n")
SquareFeet=int(input("Enter the size of the stall in square feet:\n"))
numberofTV=input("Does the hall have TV?(y/n)\n")
if (numberofTV=='y'):
    numberofTV=int(input("Enter the number of TV:\n"))
    obj=Stall(name,det,on)
    obj.computeCost(StallType,SquareFeet,numberofTV)
elif (numberofTV=='n'):
    numberofTV=0
    obj=Stall(name,det,on)
    obj.computeCost(StallType,SquareFeet,numberofTV)
