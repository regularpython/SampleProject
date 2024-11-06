
# a = 2
# b = 2
#
# c = a + b
#
# print(c)

# def addition(c, d):
#     a = c
#     b = d
#     c = a + b
#     print(c)
#
#
# addition(2,3)


class MathOperation:
    def addition(self, c, d):
        a = c
        b = d
        c = a + b
        print(c)

    def subtrcation(self, c, d):
        e = c-d
        print(e)

obj = MathOperation()
obj.addition(3,5)
obj.subtrcation(5,2)