from curses.ascii import isalpha
import random
form words import word_list



def run():
   
   def get_word():
      word = random.choice(word_list)
      return word.upper()


   def play(word):
      word_completion = "_" * len(word)
      guessed = False
      guessed_letters = []
      guessed_words = []
      tries = 7
      print("lets play hangman!!!")
      print(displayed_hangman(tries))
      print("\n")
      while not guessed and tries > 0:
         guess = input ("please guess a letter for this word: ").upper()
         if len(guess) == 1 and guess.isalpha():
         
         elif len(guess) == len(word) and guess.isalpha




   



   def displayed_hangman(tries):
      stages = ["""

               --------------------
               ---------V----------
                        |
                        |
                        0
                      \ | /
                        |
                       /?\
                      /   \ 
               ""","""

               --------------------
               ---------V----------
                        |
                        |
                        0
                      \ | /
                        |
                       /?
                      /    
               """,
               """

               --------------------
               ---------V----------
                        |
                        |
                        0
                      \ | /
                        |



               ""","""

               --------------------
               ---------V----------
                        |
                        |
                        0
                      \ | 
                        |

                      
                        
               """,
               """

               --------------------
               ---------V----------
                        |
                        |
                        0
                        | 
                        |

                      
                        
               """,
               """

               --------------------
               ---------V----------
                        |
                        |
                        0
                        


                      
                        
               ""","""

               --------------------
               ---------V----------
                        |
                       

                     
                        
                        

                      
                        
               """]





if __name__=="__main__":
    run()