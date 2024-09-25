# Developed by Numan Salahuddin
# Student Number: 251264939
# Description: Program made to take order of the dishes for number of invitees and produce the cost for each.


#Declaring a function with if-else statements for dishes.
def dish(k,v,g):
    if k == "y" and v == "y" and g != "y":
        dish = "pizza"
    elif k != "y" and v == "y" and g != "y":
        dish = "pasta"
    elif k == "y" and v == "y" and g == "y":
        dish = "falafel"
    elif k == "y" and v!= "y" and g == "y":
        dish = "steak"
    else:
        dish = "beverage"
    return dish
# Input for number of invitees.
no_of_inv = int(input("Please enter number of invitees: "))
print()
# Number of dishes ordered with empty list of Invitees.
inv_list = []
pizza = 0
pasta = 0
falafel = 0
steak = 0
beverage = 0

# For loop used for the questions of the order to the invitees.
for i in range(no_of_inv):
    temp=[]  # temp takes order for each of them and adds to main list, after the first loop temp is null and accepts value for second.
    print("Please enter the order detials for invitee Number " , i+1 , "/" , no_of_inv)
    keto = input("Do you want a keto friendly meal?")
    vegan = input("Do you want a vegan meal?")
    gluten = input("Do you want a Gluten-free meal?")
    dish_ = dish(keto,vegan,gluten)
    temp.append(keto)
    temp.append(vegan)
    temp.append(gluten)
    temp.append(dish_)
    if temp[3] == "pizza":
        pizza += 1
    if temp[3] == "pasta":
        pasta += 1
    if temp[3] == "falafel":
        falafel += 1
    if temp[3] == "steak":
        steak += 1
    if temp[3] == "beverage":
        beverage += 1
    inv_list.append(temp)
    print("-------------------------")

# Declaring each dishes variable cost values
pizza_cost = pizza * 44.50
pasta_cost = pasta * 48.99
falafel_cost = falafel * 52.99
steak_cost = steak * 49.60
beverage_cost = beverage * 5.99

# Input for the tip after dishes ordered.
tip = int(input("How much do you want to tip your server (% percent)?"))
print()

# Printing the output of the receipt after order taken.
print("You have " , no_of_inv , " with the following orders:")
print(pizza , " invitees ordered Pizza. The cost is: $%.2f" %pizza_cost)
print(pasta , " invitees ordered Pasta. The cost is: $%.2f" %pasta_cost)
print(falafel , " invitees ordered Falafel. The cost is: $%.2f" %falafel_cost)
print(steak , " invitees ordered Steak. The cost is: $%.2f" %steak_cost)
print(beverage, " invitees ordered only beverage. The cost is: $%.2f" %beverage_cost)
print()

# Prints the cost for everything.
total = round(pizza_cost,2) + round(pasta_cost,2) + round(falafel_cost,2) + round(steak_cost,2) + round(beverage_cost,2)
print("The total cost before tax is $" + str(round(total,2)))
total = total * (100 + 13)/100
print("The total cost after tax is $" + str(round(total,2)))
total = total * (100 + tip)/100
print("The total cost after " , str(tip) + "% tip is $" + str(round(total)))
