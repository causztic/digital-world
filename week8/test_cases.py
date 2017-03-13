from Coordinate import Coordinate

p = Coordinate()
print p.x , p.y
print p.magnitude()
p.x = 3
p.y = 4
print p.magnitude()
q = Coordinate(3 ,4)
print p == q
q.translate(1 , 2)
print q.x
print p == q