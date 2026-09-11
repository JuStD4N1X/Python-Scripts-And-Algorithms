import unittest
from main import Dice

class TestDiceGame(unittest.TestCase):

    def test_value_between_1_and_6(self):
        dice = Dice()
        dice.throwing()
        self.assertIn(dice.dice_amount, [1, 2, 3, 4, 5, 6])

    def test_roll_does_not_change_value_when_blocked(self):
        dice = Dice()
        initial_value = dice.dice_amount

        dice.blocking()
        for _ in range(100):
            dice.throwing()

        self.assertEqual(dice.dice_amount, initial_value)


if __name__ == '__main__':
    unittest.main()