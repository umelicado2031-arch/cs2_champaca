import math

# Ask the user to enter the coordinates of the first point
x1 = float(input("Enter x1:"))
x2 = float(input("Enter x2:"))

# Ask the user to enter the coordinates of the second point
y1 = float(input("Enter y1:"))
y2 = float(input("Enter y2:"))

# Compute the distance using the distance formula
distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

point_a=pow(x2-x1,2)
point_b=pow(y2-y1,2)
distance=math.sqrt(point_a+point_b)

# Display the result rounded to two decimal places
print("The distance: ", distance)
