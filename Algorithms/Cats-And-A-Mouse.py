def catAndMouse(x, y, z):

    a = abs(x-z)
    b = abs(y-z)

    return "Cat A" if a<b else "Cat B" if b<a else "Mouse C"

x = 2
y = 1
z = 3
catAndMouse(x,y,z)
