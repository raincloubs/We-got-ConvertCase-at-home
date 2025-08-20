# Importd the needed modules
import sys

# Asks the user to type something and the program will spit out upper and lower case versions
while True:
 typed_words = input("Type your word and or words: ")
 print(typed_words.upper())
 print(typed_words.lower())
 print(typed_words.title())

# Breaks the loop and quits the program
 if typed_words.lower() == "quit":
  break