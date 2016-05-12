from A.classes import Animal, Poacher, Tourist     #importing specific function
from A.functions import word_count, sum_of_digits


print Animal, word_count


#importing the whole module
import A.functions as func 
import A.classes as classes

print classes.Animal, func.word_count