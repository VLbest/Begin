# MD5 hash calculator

from InputManager import InputManager
from MD5 import MD5

inputManager = InputManager()
md5Hash = MD5() 


inputManager.message = inputManager.readInput()
print("\nYour messsage is: \n"+inputManager.message);
print("\n----start----\n")
res = md5Hash.getMD5HashOf(inputManager.message)

