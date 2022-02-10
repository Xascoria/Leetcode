class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        guess_wrong_guess = {}
        guess_wrong_ans = {}
        guess_correct = 0
        for i,j in zip(guess, secret):
            if i == j:
                guess_correct += 1
            else:
                guess_wrong_guess[i] = guess_wrong_guess.get(i,0) + 1
                guess_wrong_ans[j] = guess_wrong_ans.get(j,0) + 1
                
        wrong_pos = 0
        for i in guess_wrong_ans:
            wrong_pos += min( guess_wrong_ans[i], guess_wrong_guess.get(i,0) )
        return f"{guess_correct}A{wrong_pos}B"