import os
import time

index = 0
while(True):

	time.sleep(10)
	os.system("taskkill /F /im solver.exe")
	print(str(index))
	index += 1
