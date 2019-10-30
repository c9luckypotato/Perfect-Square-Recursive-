#Jordan An
#09/22/2019
#The program calculate the weight of the ice cream in 

# Import the Holy Bible of math
import math
# Define the height, the diameter and the radius of the cone
h = 5.25
d = 2
r = d/2

# Compute the total volume of the ice cream cone using V = pi*r^2*h/3
# for the cone and V = 2/3 * pi * r^3 for the hemisphere, sum them up
V_total = (math.pi * math.pow(r, 2) * h/3) + (2/3 * math.pi * math.pow(r, 3))

# Converting 1 gallon and 0.1336 cubic feet to cubic inch for unit consistency
gallon   = 1 * 231
cub_feet = 0.1336 * 12**3

# Compute the weight of the ice cream that can fit in the cone in ounce
W = (1.5/ (gallon * cub_feet)) * V_total *16

# Print out for the user
print("The weight of the ice cream that can fit in the cone is %f oz" %W)

# I used google to know how to convert these units
# Please give us a problem in metric next time
