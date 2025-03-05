import unittest
from main import play_game

class TestPlayGame(unittest.TestCase):

   def test_player_wins(self):
       self.assertEqual(play_game("Rock","Scissors"),"You win!")

   def test_player_lose(self):
       self.assertEqual(play_game("Scissors", "Rock"),"You lose!")

   def test_player_tie(self):
       self.assertEqual(play_game("Rock","Rock"),"It's a tie!")


if __name__ == '__main__':
    unittest.main()
