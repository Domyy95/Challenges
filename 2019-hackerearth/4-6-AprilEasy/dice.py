dice_throws = list(input())

if len(dice_throws) > 100000:
	print(-1)
else: 
	girls = 0
	illegale = False
	for throw in dice_throws:
	    if 6 > int(throw) > 0:
	        girls = girls + 1
	    elif(int(throw) != 6):
	    	illegale = True

	if illegale == True:
		print(-1)
	elif len(dice_throws) > 0 and girls == 0:
	    print(-1)
	elif len(dice_throws) == 0:
		print(-1)
	elif dice_throws[len(dice_throws)-1] == str(6):
		print(-1)
	else:
	    print(girls)
