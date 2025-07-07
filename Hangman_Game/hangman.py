import tkinter as tk
import random
from hangman_words import countries
# Example word list with hints


hangman_text = '''Hangman Globe'''

stages = [
    '''  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========= ''',
    '''  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n========= ''',
    '''  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n========= ''',
    '''  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n========= ''',
    '''  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n========= ''',
    '''  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n========= ''',
    '''  +---+\n  |   |\n      |\n      |\n      |\n      |\n========= '''
]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title(hangman_text)
        self.lives = 6
        self.chosen_word, self.hint = random.choice(list(countries.items()))
        self.correct_letters = []
        self.display = ""
        self.placeholder = "_"
        self.word_length = len(self.chosen_word)
        self.game_over = False

        self.label_title = tk.Label(root, text=hangman_text, font=("TimesNewRoman 20 bold"))
        self.label_title.pack()

        self.label_word = tk.Label(root, text=" ".join(self.placeholder), font=("Consolas", 22))
        self.label_word.pack(pady=10)

        self.label_lives = tk.Label(root, text=f"Lives: {self.lives}/6", font=("Segoe", 14))
        self.label_lives.pack()

        self.label_hint = tk.Label(root, text=f"Hint: {self.hint}", font=("Segoe", 12), fg="blue")
        self.label_hint.pack()

        self.hangman_canvas = tk.Label(root, text=stages[6], fg="red", font=("Courier", 12), justify="left")
        self.hangman_canvas.pack()

        self.entry = tk.Entry(root, font=("Helvetica", 14), width=5)
        self.entry.pack()

        self.button = tk.Button(root, text="Guess", command=self.game_over_func)
        self.button.pack(pady=10)

        self.message = tk.Label(root, text="", font=("Helvetica", 12), fg="red")
        self.message.pack()

        self.play_again_button = tk.Button(root, text="Play Again", command=self.restart_game, state="disabled")
        self.play_again_button.pack(pady=5)

        self.position_underscore()

    def position_underscore(self):
        self.placeholder = "_" * self.word_length
        print(self.placeholder)

    def game_over_func(self):
        if self.game_over:
            return

        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(guess) != 1:
            self.message.config(text="Invalid letter!")
            return

        if guess in self.correct_letters:
            self.message.config(text=" You already guessed that letter!")
            return

        if guess in self.chosen_word:
            self.correct_letters.append(guess)

        self.display = ""

        for letter in self.chosen_word:
            if letter in self.correct_letters:
                self.display += letter
            else:
                self.display += "_"

        self.label_word.config(text=" ".join(self.display))

        if guess not in self.chosen_word:
            self.lives -= 1
            self.label_lives.config(text=f"Lives Remain: {self.lives}/6", font=("Segoe", 14))
            self.message.config(text=f"OOPs !! You Choose a Wrong letter {guess}")
            self.hangman_canvas.config(text=stages[6 - self.lives])
            if self.lives == 0:
                self.game_over = True
                self.label_word.config(text=self.chosen_word)
                self.message.config(text="!!You Loss!!")
                self.play_again_button.config(state="normal")
        if "_" not in self.display:
            self.game_over = True
            self.message.config(text="🎉 You Win!")
            self.play_again_button.config(state="normal")

    def restart_game(self):
        self.lives = 6
        self.chosen_word, self.hint = random.choice(list(countries.items()))
        self.correct_letters = []
        self.display = ""
        self.word_length = len(self.chosen_word)
        self.game_over = False
        self.placeholder = "_" * self.word_length

        self.label_word.config(text=" ".join(self.placeholder))
        self.label_lives.config(text=f"Lives: {self.lives}/6")
        self.hangman_canvas.config(text=stages[6])
        self.label_hint.config(text=f"Hint: {self.hint}")
        self.message.config(text="")
        self.entry.delete(0, tk.END)
        self.play_again_button.config(state="disabled")

root = tk.Tk()
game = HangmanGame(root)
root.mainloop()
