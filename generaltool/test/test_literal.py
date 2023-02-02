from unittest import TestCase
from generaltool import enforce_literals, Literal

class TestLiteral(TestCase):
    def test_without(self):
        def x(foo: Literal[1, 2]):
            return foo

        self.assertEqual(1, x(1))
        self.assertEqual(2, x(2))
        self.assertEqual(3, x(3))

    def test_one(self):
        def x(foo: Literal[1, 2]):
            enforce_literals(x)
            return foo

        self.assertEqual(1, x(1))
        self.assertEqual(2, x(2))
        self.assertRaises(AssertionError, x, 3)

    def test_class(self):
        class X:
            def x(self, foo: Literal[1, 2]):
                enforce_literals(X.x)
                return foo

        self.assertEqual(1, X().x(1))
        self.assertEqual(2, X().x(2))
        self.assertRaises(AssertionError, X().x, 3)

    def test_two(self):
        def x(a: Literal[1, 2], b: Literal["foo"]):
            enforce_literals(x)
            return a, b

        self.assertEqual((1, "foo"), x(1, "foo"))
        self.assertEqual((2, "foo"), x(2, "foo"))
        self.assertRaises(AssertionError, x, 3, "foo")
        self.assertRaises(AssertionError, x, 2, "bar")
        self.assertRaises(AssertionError, x, None, "foo")
        self.assertRaises(AssertionError, x, 1, None)
        self.assertRaises(AssertionError, x, 1, "")

    def test_three(self):
        def x(a: Literal[1, 2], b, c: Literal["foo", "", None] = "bar"):
            enforce_literals(x)
            return a, b, c

        self.assertEqual((1, None, "foo"), x(1, None, "foo"))
        self.assertEqual((2, 5, "foo"), x(2, 5, "foo"))
        self.assertRaises(AssertionError, x, 3, "foo")
        self.assertRaises(AssertionError, x, 2, "bar")
        self.assertRaises(AssertionError, x, None, "foo")
        self.assertRaises(AssertionError, x, 1, None)
        self.assertRaises(AssertionError, x, 1, "")
        self.assertRaises(AssertionError, x, 1, "hi")

    def test_mixed(self):
        def x(a: Literal[1, "two", None]):
            enforce_literals(x)
            return a

        self.assertEqual(1, x(1))
        self.assertEqual("two", x("two"))
        self.assertEqual(None, x(None))
        self.assertRaises(AssertionError, x, ...)
        self.assertRaises(AssertionError, x, 0)
        self.assertRaises(AssertionError, x, "")

    def test_empty(self):
        def x(a: Literal[""]):
            enforce_literals(x)
            return a

        self.assertEqual("", x(""))
        self.assertRaises(AssertionError, x, ...)
        self.assertRaises(AssertionError, x, 0)
        self.assertRaises(AssertionError, x, "hi")

    def test_zero(self):
        def x(a: Literal[0]):
            enforce_literals(x)
            return a

        self.assertEqual(0, x(0))
        self.assertEqual(0, x(0.0))
        self.assertRaises(AssertionError, x, "0")
        self.assertRaises(AssertionError, x, "")

    def test_return_type_hint(self):
        def x(foo: Literal[1, 2]) -> int:
            enforce_literals(x)
            return foo

        self.assertEqual(1, x(1))
        self.assertEqual(2, x(2))
        self.assertRaises(AssertionError, x, 3)
























