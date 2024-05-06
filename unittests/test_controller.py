import unittest
from controller import Controller

class TestController(unittest.TestCase):
    def test_init(self) -> None:
        st7796_controller = Controller(someDriver, [])
        tests = [
            {
                "operand":0,
                "result":1,
                "correct":True,
            }
        ]
        for test in tests:
            with self.subTest( f"{test['operand']}!"):
                if test["correct"]:
                    self.assertEqual(test["operand"], test["result"])
                else:
                    with self.assertRaises(AssertionError):
                        self.assertEqual(test["operand"], test["result"])