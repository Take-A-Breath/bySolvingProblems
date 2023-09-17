# At Chip's Fast Food emporium there is a very simple menu. Each food item is selected by entering a digit choice.
# 
#  Here are the three burger choices:
#     1 – Cheeseburger (461 Calories)
#     2 – Fish Burger (431 Calories)
#     3 – Veggie Burger (420 Calories)
#     4 – no burger
# 
#  Here are the three drink choices:
#     1 – Soft Drink (130 Calories)
#     2 – Orange Juice (160 Calories)
#     3 – Milk (118 Calories)
#     4 – no drink
# 
#  Here are the three side order choices:
#     1 – Fries (100 Calories)
#     2 – Baked Potato (57 Calories)
#     3 – Chef Salad (70 Calories)
#     4 – no side order
# 
#  Here are the three dessert choices:
#     1 – Apple Pie (167 Calories)
#     2 – Sundae (266 Calories)
#     3 – Fruit Cup (75 Calories)
#     4 – no dessert
# 
# The program should input a number for each type of item then calculate and display the Calorie total. The first line will be the customer's
# choice of burger, the second will be the choice of side, then drink, then dessert. You may assume that each input will be a number from 1 to 4
# That is, each customer has to pick exactly one number from each of the four options out of each of the four categories.
# 
# The program prints out the total Calories of the selected meal, and stops executing after this output.

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

if burger == 1:
    burger = 461
elif burger == 2:
    burger = 431
elif burger == 3:
    burger = 420
else:
    burger = 0

if side == 1:
    side = 100
elif side == 2:
    side = 57
elif side == 3:
    side = 70
else:
    side = 0

if drink == 1:
    drink = 130
elif drink == 2:
    drink = 160
elif drink == 3:
    drink = 118
else:
    drink = 0

if dessert == 1:
    dessert = 167
elif dessert == 2:
    dessert = 266
elif dessert == 3:
    dessert = 75
else:
    dessert = 0

total_calories = (burger + side + drink + dessert)

print('Your total Calorie count is ' + str(total_calories) + '.')
