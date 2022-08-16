class variables_test:
    # Global Variable
    a = 20
    # if we declare any variable inside the class is called global variable

    def test_one(self):
        b = 40  # if we declare any variable inside the method and outside the class is called local variable
        print(b)
        print(variables_test.a)

    def test_two(self):
        c = 60
        print(c)
        print(variables_test.a)


t = variables_test()
t.test_one()
t.test_two()
