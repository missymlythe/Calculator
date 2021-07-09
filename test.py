import unittest
from main import Logic, Calculator

#   -   -   -   -   -   -   C A L C U L A T O R  L O G I C  T E S T S  -   -   -   -   -   -   #
class Test(unittest.TestCase):
    def test_normal(self):
        g = Logic()
        g.input = "5"
        self.assertEqual(g.evaluate(), '5')
    
    def test_add(self):
        g = Logic()
        g.input = "1 + 1"
        self.assertEqual(g.evaluate(), "2" )

    def test_add2(self):
        g = Logic()
        g.input = "2 + 2 + 2"
        self.assertEqual(g.evaluate(), '6')

    def test_subtract(self):
        g = Logic()
        g.input = "2 - 5 "
        self.assertEqual(g.evaluate(), '-3')

    def test_subtract2(self):
        g = Logic()
        g.input = "27 - 16"
        self.assertEqual(g.evaluate(), '11')

    def test_subtract3(self):
        g = Logic()
        g.input = "5 - 5 - 5"
        self.assertEqual(g.evaluate(), '-5')

    def test_multiply(self):
        g = Logic()
        g.input = "5 * 5"
        self.assertEqual(g.evaluate(), '25')

    def test_multiply2(self):
        g = Logic()
        g.input = "327 * 9 * 0"
        self.assertEqual(g.evaluate(), '0')

    def test_divide(self):
        g = Logic()
        g.input = "1 / 1"
        self.assertEqual(g.evaluate(), '1.0' )
    
    def test_divide2(self):
        g = Logic()
        g.input = "10 / 2"
        self.assertEqual(g.evaluate(), '5.0')

    def test_complex(self):
        g = Logic()
        g.input = "92 * 2 / 5"
        self.assertEqual(g.evaluate(), '36.8')

    def test_complex2(self):
        g = Logic()
        g.input = "14253 - 5375628 / 5"
        self.assertEqual(g.evaluate(), '-1060872.6')

    def test_square(self):
        g = Logic()
        g.input = "5"
        self.assertEqual(g.square(), '25')
    
    def test_sqrt(self):
        g = Logic()
        g.input = "81"
        self.assertEqual(g.sqrt(), '9.0')

    def test_percent(self):
        g = Logic()
        g.input = "90"
        self.assertEqual(g.percent(), '0.9')

    def test_sin(self):
        g = Logic()
        g.input = "0"
        self.assertEqual(g.sin(), '0.0')

    def test_cos(self):
        g = Logic()
        g.input = "0"
        self.assertEqual(g.cos(), '1.0')

    def test_tan(self):
        g = Logic()
        g.input = "0"
        self.assertEqual(g.tan(), '0.0')


#   -   -   -   -   -   -   C A L C U L A T O R  G U I  T E S T S  -   -   -   -   -   -   #
    
    def test_add_gui(self):
        self.c = Calculator()
        self.c.add_expression("1")
        self.c.add_expression("2")
        self.c.add_operator("+")
        self.c.add_expression("2")
        self.c.evaluate()

        self.assertEqual(self.c.expression, "14", msg=None)

        self.c.clear()

    def test_subtract_gui(self):
        self.c = Calculator()
        self.c.add_expression("5")
        self.c.add_expression("0")
        self.c.add_operator("-")
        self.c.add_expression("10")
        self.c.evaluate()

        self.assertEqual(self.c.expression, "40", msg=None)

        self.c.clear()

    def test_multiply_gui(self):
        self.c = Calculator()
        self.c.add_expression("1")
        self.c.add_expression("0")
        self.c.add_operator("*")
        self.c.add_expression("5")
        self.c.evaluate()

        self.assertEqual(self.c.expression, "50", msg=None) 

        self.c.clear()

    def test_divide_gui(self):
        self.c = Calculator()
        self.c.add_expression("1")
        self.c.add_expression("0")
        self.c.add_operator("/")
        self.c.add_expression("5")
        self.c.evaluate()

        self.assertEqual(self.c.expression, "2.0", msg=None) 

        self.c.clear()

    def test_square_gui(self):
        self.c = Calculator()
        self.c.add_expression("2")
        self.c.square()

        self.assertEqual(self.c.expression, "4", msg=None)

        self.c.clear()

    def test_sqrt_gui(self):
        self.c = Calculator()
        self.c.add_expression("4")
        self.c.sqrt()

        self.assertEqual(self.c.expression, "2.0", msg=None)

        self.c.clear()

    def test_percent_gui(self):
        self.c = Calculator()
        self.c.add_expression("5")
        self.c.add_expression("1")
        self.c.add_expression("3")
        self.c.percent()

        self.assertEqual(self.c.expression, "5.13", msg=None)

        self.c.clear()

    def test_percent2_gui(self):
        self.c = Calculator()
        self.c.add_expression("9")
        self.c.add_expression("0")
        self.c.add_operator("*")
        self.c.add_expression("3")
        self.c.add_expression("0")
        self.c.percent()
        self.c.evaluate()

        self.assertEqual(self.c.expression, "27.0", msg=None)

        self.c.clear()

    def test_decimal_gui(self):
        self.c = Calculator()
        self.c.add_expression("1")
        self.c.add_expression(".")
        self.c.add_expression("5")
        self.c.add_operator("*")
        self.c.add_expression("2")
        self.c.evaluate()

        self.assertEqual(self.c.expression, "3.0", msg=None)

        self.c.clear()

    def test_delete_gui(self):
        self.c = Calculator()
        self.c.add_expression("5")
        self.c.add_expression("7")
        self.c.add_expression("1")
        self.c.delete()

        self.assertEqual(self.c.expression, "57", msg=None)

    def test_delete_gui2(self):
        self.c = Calculator()
        self.c.add_expression("4")
        self.c.add_expression("8")
        self.c.add_expression("3")
        self.c.add_expression(".")
        self.c.add_expression("5")
        self.c.add_operator("*")
        self.c.add_expression("6")
        self.c.add_expression("8")
        self.c.add_operator("+")
        self.c.delete()

        self.assertEqual(self.c.total, "483.5*68", msg=None)

        self.c.clear()

    def test_sin_gui(self):
        self.c = Calculator()
        self.c.add_expression("6")
        self.c.add_expression("0")
        self.c.sin()

        self.assertEqual(self.c.expression, "-0.3048106211022167", msg=None)

        self.c.clear()

    def test_cos_gui(self):
        self.c = Calculator()
        self.c.add_expression("9")
        self.c.add_expression("0")
        self.c.cos()

        self.assertEqual(self.c.expression, "-0.4480736161291701", msg=None)

        self.c.clear()

    def test_trigo_gui(self):
        self.c = Calculator()
        self.c.add_expression("0")
        self.c.tan()
        self.c.add_operator("+")
        self.c.add_expression("9")
        self.c.add_operator("*")
        self.c.add_expression("0")

        self.assertEqual(self.c.expression, "0", msg=None)

        self.c.clear()

    def test_trig02_gui(self):
        self.c = Calculator()
        self.c.add_expression("0")
        self.c.cos()
        self.c.add_operator("+")
        self.c.add_expression("9")
        self.c.add_operator("/")
        self.c.add_expression("3")

        self.assertEqual(self.c.expression, "3", msg=None)

        self.c.clear()




if __name__ == "__main__":
    unittest.main()
