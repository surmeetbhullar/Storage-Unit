import numpy as np

storage = np.array([])

def mainmenu():
  print("1. Add an Item")
  print("2. Remove an Item")
  print("3. Find an Item")
  print("4. Display the Storage")
  print("5. Quit")
  
i = 0
while i==0:
  t = "t"
  mainmenu()
  prompt = float(input())
  if prompt == 1:
    print("Please enter the name of the item you would like to add: ")
    text = str(input())
    storage = np.append(storage, text)
  elif prompt == 2:
    if len(storage) <= 0:
      print("The list is empty.")
    else:
      storage = np.delete(storage, len(storage) - 1)
      print(text + " was removed from the storage.")
  elif prompt == 3:
    print("Please enter the name of the item you would like to find: ")
    text = str(input())
    i = 0
    for box in storage:
      if box == text:
        print(text + " was found in the storage.")
        break
        i += 1
      elif len(storage) >= i:
        print(text + " was not found in the storage.")
  elif prompt == 4:
    print(storage)
  elif prompt == 5:
    i = 1
  
