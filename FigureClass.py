import math

class Circle ():
    def __init__(self):
        while True:
            try:
                self.radius = int(raw_input('Please enter radius: '))
                break
            except ValueError:
                print 'That is not number. Please try again...'
    def area(self):
        return self.radius * self.radius * math.pi

class Triangle ():
    def __init__(self):
        while True:
            try:
                self.height = int(raw_input('Please enter triangle Height: '))
                self.side = int(raw_input('Please enter triangle Side: '))
                break
            except ValueError:
                print 'That is not number. Please try again...'
    def area(self):
        return self.side / 2 * self.height


class Rectangle():
    def __init__(self):
        while True:
            try:
                self.height = int(raw_input('Please enter rectangle Height: '))
                self.length = int(raw_input('Please enter rectangle Length: '))
                break
            except ValueError:
                print 'That is not number. Please try again...'
    def area(self):
        return self.height * self.length

if __name__ == '__main__':
    data = None
    f = raw_input('Please enter figure: ')
    if f in ('circle', 'triangle', 'rectangle'):
        if f == 'circle':
            data = Circle()
        elif f == 'triangle':
            data = Triangle()
        elif f == 'rectangle':
            data = Rectangle()
        print data.area()
    else:
        print 'Figure is not correct'











