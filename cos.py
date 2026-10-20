import math
b = int(input())
c = int(input())
d = int(input())
d = math.radians(d)
cosd=math.cos(d)
a = math.sqrt(b*b+c*c-2*b*c*cosd)
print (a)
