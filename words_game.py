from config import LETTERS_POINTS

class ScorePlayer:
    #at first each player has no score
    player_1 = 0
    player_2 = 0

    @classmethod
    # for each letter in the word of a player, player can get score
    def calculate_word_score(self, word):
        score = 0
        if word.isalpha():

            for letter in word.lower():
                score += LETTERS_POINTS[letter]

            return score

        else:
            raise ValueError


    @classmethod    
    # the player who has more score will be the winner of the game
    def find_winner(self, word1, word2):
        if self.calculate_word_score(word1) > self.calculate_word_score(word2):
            return 'First Player Won'

        elif self.calculate_word_score(word1) < self.calculate_word_score(word2):
            return 'Second Player Won'

        else:
            return 'Draw'

