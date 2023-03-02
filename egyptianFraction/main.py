from fractions import Fraction

#given a fraction, represent it in egyptian format

input = input("Input Fraction Here: ")
current = Fraction(input)#value left over of input after every iteration
i = 2
series = Fraction(1,i) #1/2, 1/3, ... , 1/n
result = []
while 1:
	if series == current:
		result.append(series)
		break
	if current > series:
		result.append(series)
		current = current - series
		i += 1
		series = Fraction(1,i)
	else:
		i+=1
		series = Fraction(1,i) #this part takes the longest
	
#this gives minimum amount of fractions
#in egyptian format
print(result)
	
	
		
		
		
		
	



