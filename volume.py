x = input("Find area of:circle/square/rectangle:")

if x == 'circle':
 rad = int(input('Enter radius of the sphere:'))
 area = (3.14159)*(rad*rad)
 print(area)

elif x == 'square':
 side = int(input("Enter the side of a square:"))
 area = (side*side)
 print(area)

elif x == 'rectangle':
 length = int(input("Enter the length of rectangle:"))
 readth = int(input("Enter the breadth of the rectangle:"))
 area = length*breadth
 print(area)
 