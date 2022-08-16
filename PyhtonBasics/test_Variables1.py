# class test_variables:
# Global Variable
a = 20  # if we declare any variable inside the class is called global varibale


def test1():
    b = 40  # if we declare any variable inside the method and outside the class is called local variable
    global a
    print(a)
    print(b)


test1()
