class Stall: 
    def __init__(self,name,det,on):
        self.name=name
        self.det=det
        self.on=on
    
    def computeCost(self,StallType,SquareFeet,numberofTV):
        self.StallType=StallType
        self.SquareFeet=SquareFeet
        self.numberofTV=numberofTV
        self.tcost=10000*self.numberofTV
        if (self.StallType=='Platinum'):
            self.cost=200*self.SquareFeet
            print("The cost of the stall is",float(self.cost+self.tcost))
        elif (self.StallType=='Diamond'):
            self.cost=150*self.SquareFeet
            print("The cost of the stall is",float(self.cost+self.tcost))
        elif (self.StallType=='Gold'):
            self.cost=100*self.SquareFeet
            print("The cost of the stall is",float(self.cost+self.tcost))
