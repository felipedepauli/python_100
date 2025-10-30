import random

def print_header():
    print("----------------")
    print("Hanging Game")
    print("----------------")

all_words = [
    "python", "algorithm", "variable", "function", "integer", "string", "boolean", "list", "tuple", "dictionary", "loop", "condition", "object", "class", "method", "inheritance", "encapsulation", "polymorphism", "recursion", "iteration", "exception", "module", "package", "import", "lambda", "generator", "comprehension", "decorator", "syntax", "debugging", "compile", "execute", "statement", "operator", "argument", "parameter", "return", "break", "continue", "pass", "global", "local", "scope", "index", "slice", "append", "extend", "insert", "remove", "pop", "sort", "reverse", "count", "copy", "clear", "update", "keys", "values", "items", "setdefault", "get", "enumerate", "zip", "map", "filter", "reduce", "random", "math", "time", "datetime", "os", "sys", "json", "pickle", "thread", "process", "queue", "stack", "heap", "tree", "graph", "search", "sort", "merge", "split", "join", "read", "write", "open", "close", "flush", "seek", "with", "try", "except", "finally", "raise", "assert", "input", "output", "print"
]

STAGES = [
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

def reveal_letters(letter, word, word_unveiled):
    """Reveals the positions of the guessed letter in the word."""
    return "".join(
        [letter if word[i] == letter else word_unveiled[i] for i in range(len(word))]
    )

def main():
    print_header()
    word = random.choice(all_words)
    word_unveiled = "_" * len(word)
    letters_called = set()
    current_state = 0

    while True:
        print(STAGES[current_state])
        print("Word:", " ".join(word_unveiled))
        if current_state == len(STAGES) - 1:
            print("You died... Ashamed of you!")
            break

        letter = input("\nWhat's the letter? ").strip().lower()
        if not letter or len(letter) != 1 or not letter.isalpha():
            print("--- Please enter a single valid letter! ---")
            continue

        if letter in letters_called:
            print("--- You've already said that letter! ---")
            continue

        letters_called.add(letter)
        new_word_unveiled = reveal_letters(letter, word, word_unveiled)

        if new_word_unveiled == word_unveiled:
            current_state += 1
        else:
            word_unveiled = new_word_unveiled

        if "_" not in word_unveiled:
            print("You won!")
            print("The word was:", word)
            break

        print("------------------------------------------")

if __name__ == "__main__":
    main()
