from collections import namedtuple 


Color = namedtuple('Color', ['r', 'g', 'b'])
c = Color(r=55, g=100, b=150)

print(c.r)