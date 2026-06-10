# CodeAlpha__task__1
# Hangman Game in Python

A classic command-line Hangman game built using Python. The game randomly selects a secret word from a predefined list, and the player must guess it letter by letter within a limited number of attempts.

---

## 🎮 How to Play

1. **Setup:** Run the script and enter your player name.
2. **The Objective:** Guess the hidden word represented by underscores (`_ _ _ _`).
3. **Guessing:** Input one alphabetic letter at a time.
4. **Scoring & Lives:**
   * You start with **6 chances**.
   * A **correct guess** reveals the letter's position(s) and keeps your chances the same.
   * A **wrong guess** costs you 1 chance.
5. **Winning:** Reveal all the letters of the word before running out of chances.
6. **Losing:** If your remaining choices drop to 0, it's Game Over!

---

## 🛠️ Key Features

* **Smart Input Validation:** Checks to ensure you only enter a single alphabetic character (prevents wasting turns on numbers, symbols, or accidental multi-letter inputs).
* **Duplicate Guess Protection:** Reminds you if you have already guessed a specific letter so you don't lose lives unfairly.
* **Clean Text UI:** Utilizes formatted ASCII-style banners for a retro arcade feel.
* **Diverse Word Bank:** Includes built-in tech and everyday words like *algorithm*, *background*, *mango*, and *python*.

---

## 💻 Technical Requirements

* **Python 3.x** installed on your system.
* No external libraries needed (uses Python's built-in `random` module).

---

## 🚀 How to Run the Game

1. **Clone or Download** the project files.
2. Open your terminal or command prompt and navigate to the folder containing the script.
3. Run the following command:

```bash
python hangman.py
