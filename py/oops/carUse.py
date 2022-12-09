from oops import Car

c1 = Car('car1', 'volvo' ,'1999', 'green')
c2 = Car('car2', 'volvo1' ,'1991', 'green1')

print(c1.make)
print(c1.model)
print(c1.year)
print(c1.color)
print(c2.make)
print(c2.model)
print(c2.year)
print(c2.color)

c1.drive()
c2.stop()
    