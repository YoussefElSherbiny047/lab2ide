humanage= 12
dogage=humanage*7
dogmonths = int((dogage-int(dogage))*12)
dogdays= int((((dogage-int(dogage))*12)-int(((dogage-int(dogage))*12)))*30)
print('Enter your age:', humanage)
print('Your age in dog years is', int(dogage), 'years' , dogmonths, 'months', dogdays, 'days')

catage=humanage/9
catmonths = int((catage-int(catage))*12)
catdays= int((((catage-int(catage))*12)-int(((catage-int(catage))*12)))*30)
print('Your age in cat years is', int(catage), 'years' , catmonths, 'months', catdays, 'days')

horseage= 3*((((humanage**2)-47)/7)+12)
horsemonths = int((horseage-int(horseage))*12)
horsedays= int((((horseage-int(horseage))*12)-int(((horseage-int(horseage))*12)))*30)
print('Your age in horse years is', int(horseage), 'years' , horsemonths, 'months', horsedays, 'days')

