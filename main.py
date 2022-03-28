from funcion1 import funcion1
from funcion2 import funcion2
from funcion3 import funcion3
from funcion4 import funcion4
import json
if __name__ == "__main__":
  tweets = []
  with open('farmers-protest-tweets-2021-03-5.json') as file:
    maxIt = 200
    it = 0

    for line in file:
      tweets.append(json.loads(line))
      
  print(funcion1(tweets))
  print()
  print()
  print(funcion2(tweets))
  print()
  print()
  print(funcion3(tweets))
  print()
  print()
  print(funcion4(tweets))
        
  
