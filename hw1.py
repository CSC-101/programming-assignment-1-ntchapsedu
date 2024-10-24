import math
import data
from data import Employee


# Write your functions for each part in the space below.

# Part 1
#make a list of letters and then check if each letter is a vowel and if it is
def vowel_count(value:str):
    list1 = list(value)
    list2 = []
    for i in list1:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            list2.append(i)
    return len(list2)

# Part 2
#check for each list inside the list and if the list length is 2 then add that list to a new list
def short_lists(value:list[list[int]])->list:
    list1 = []
    for i in value:
        if len(i) == 2:
            list1.append(i)
    return list1
# Part 3
#check if each list inside the list is 2 values and if it is then change the order from least to biggest in that pair
def ascending_pairs(value:list[list[int]])->list:
    list1 = []
    for i in value:
        if len(i) == 2:
            if i[0] >= i[1]:
                list1.append([i[1],i[0]])
        else:
            list1.append(i)
    return list1
# Part 4
#add dollars, then add cents, while the cents are over 99 add one dollar and subtract 100 cents
def add_prices(price1, price2)->float:
    dollar_sum = price1.dollars + price2.dollars
    cent_sum = price1.cents + price2.cents
    while cent_sum > 99:
        cent_sum -= 100
        dollar_sum += 1
    price_sum = (dollar_sum + (cent_sum/100))
    return price_sum
# Part 5
#subtract the top x point from bottom x point, subtract top y point from bottom y point
def rectangle_angle(rectangle):
    side1 = abs(rectangle.top_left.x - rectangle.bottom_right.x)
    side2 = abs(rectangle.top_left.y - rectangle.bottom_right.y)
    return side1*side2
# Part 6
#for the books in list and the authors for each of those books append the title of each book that has the same author as the name
def books_by_author(name:str, books:[list[str]]):
    list1 = []
    for i in books:
        for a in i.authors:
            if a == name:
                list1.append(i.title)
    return list1
# Part 7
#find the distance between x and y values then subtract the top x and y points by half of those distances to find the center.
#for radius find euclidian distance between the two points and half that value to find radius
def circle_bound(rectangle):
    dist_x = (rectangle.top_left.x - rectangle.bottom_right.x)
    dist_y = (rectangle.top_left.y - rectangle.bottom_right.y)
    data.Circle.center = (rectangle.top_left.x - (dist_x/2),rectangle.top_left.y - (dist_y/2))
    data.Circle.radius = math.sqrt(((rectangle.top_left.x-rectangle.bottom_right.x)**2)+(rectangle.top_left.y-rectangle.bottom_right.y)**2)
    return round((data.Circle.radius/2),2),data.Circle.center

# Part 8
#add the pay rate of each person together then divide it by the amount of people.
#for each person compare their pay rate to the avg and if theirs is less them add them to a list
def below_pay_average(people:list[Employee]):
    avg = 0
    lowest = []
    for i in people:
        avg += i.pay_rate
    avg = avg/(len(people))
    for a in people:
        if a.pay_rate<avg:
            lowest.append(a.name)
    return lowest
#