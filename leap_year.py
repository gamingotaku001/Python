a=int (input("put the year you want to chack"))
if ((a%400==0 or a%4==0) (a%100!=0)):
    print("the year is leap year")
else:
    print('its not')