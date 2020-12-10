# Ebox-Internship-Assignment-Questions
STALL TYPE
  Stall Type
 
Whenever you need to perform the same operation for different types of data, using different method names for each type can be cumbersome. In these cases we use overloading. Method overloading is the ability to create multiple methods with the same name and different types of parameters. Calls to an overloaded function will run a specific implementation of that method appropriate to the type of arguments.
Write a program to calculate the cost of stall based on the stall type by overloading the compute_cost() method.

Consider stall type to be  "Gold", "Diamond", "Platinum". And they may or may not have a TV in them. So overload a method to find the cost of the stall.
Method overloading in Python is a feature that allows the same operator to have different meanings.
Create a class Stall with following attributes, 

Attribute	Datatype
name	str
detail	str
owner_name	str
   
 Include the following method in it, 

Method	Description
 compute_cost(stall_type, square_feet,number_of_tv)	This method takes stall_type, square_feet and number_of_tv(if present) as parameters and calculates and print the cost of the stall based on square feet on size and number of TV
Use the __init__() method for initializing the attributes of the Stall class.
Override __str__() method in Stall class to print the stall details

 Note: The price for various types of stalls is, Platinum = Rs.200 per sqft; Diamond = Rs.150 per sqft; Gold = Rs.100per sqft. And the price for each tv is Rs.10000. Print the final cost with one floating-point precision.

 Refer to sample input/output for further details and format of the output.

[All Texts in bold corresponds to the input and rest are output]

Sample Input and Output 1:
Enter the name of the stall:
ABC ltd
Enter the detail of the stall:
All electronics store
Enter the owner name of the stall:
XYZ
Enter the type of the stall:
Platinum
Enter the size of the stall in square feet:
1000
Does the hall have TV?(y/n)
y
Enter the number of TV:
4
Name of Stall : ABC ltd
Detail : All electronics store
Owner Name : DE
The cost of the Platinum Stall is 240000.0

 

Sample Input and Output 2 :

Enter the name of the stall:

SUV Furnitures

Enter the detail of the stall:

All furnitures available

Enter the owner name of the stall:

John

Enter the type of the stall:

Diamond

Enter the size of the stall in square feet:

250

Does the hall have TV?(y/n)

n

Name of Stall : SUV Furnitures

Detail : All furnitures available 

Owner Name : John

The cost of the Diamond Stall is 37500.0

