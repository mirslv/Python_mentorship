import math
class Circle():
    def area (self):
        while True:
            try:
                self.r = int (raw_input('Please enter radius: '))
                return self.r * self.r * math.pi
            except ValueError:
                print 'That is not a number. Please try again...'

class Triangle():
    def area (self):
        while True:
            try:
                self.height = int (raw_input('Please enter triangle Height: '))
                self.side = int(raw_input('Please enter triangle Side: '))
                return self.side / 2 * self.height
            except ValueError:
                print 'That is not a number. Please try again...'

class Rectangle():
    def area (self):
        while True:
            try:
                self.height = int (raw_input('Please enter rectangle Height: '))
                self.length = int(raw_input('Please enter rectangle Length: '))
                return self.height * self.length
            except ValueError:
                print 'That is not a number. Please try again...'

if __name__ == '__main__':
    data = ''
    f = raw_input('Please enter figure: ')
    if f == 'circle':
        data = Circle()
        print data.area()
    if f == 'triangle':
        data = Triangle()
        print data.area()
    if f == 'recangle':
        data = Rectangle()
        print data.area()
    if f not in ('circle', 'triangle', 'rectangle'):
        print 'Figure is not correct'


