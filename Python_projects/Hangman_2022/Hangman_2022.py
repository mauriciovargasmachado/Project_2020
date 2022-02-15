import random
from threading import BrokenBarrierError
import time
from words import word_list

def run():

   name = input("Please introduce your name: ")
   time.sleep(1)
   print("Hi, " + name + " Its time for some Hangman!!!")
   time.sleep(1)
   print("its time to guess!!!")
   time.sleep(1)

   def word(word_list):
      word = random.choice(word_list)
      return word.upper()

   user_word =''
   lifes=5

   while lifes > 0:
      fails = 0
      for letter in word:
         if letter in user_word:
            print(letter,end='')    
         else: 
            print(" _ ", end="")
            fails = fails + 1
      
      if fails == 0:
         print("You are a !!! W I N N E R !!!")
         time.sleep(2)
         print("!!thanks for playing!!")
         break
      
      user_letter = input("Please type a letter: ")
      user_word += user_letter

      if user_letter not in word:
         vidas -= 1
         print("the letter you choose isent in this word, try again")
         time.sleep(2)
         print("You have "+ lifes +" more")

   else:
      print("thanks for playing!!!")
   

if __name__=="__main__":
    run()