def leapyear(year):
    for i in year:
        if(i%4==0):
           if(i%100==0):
              if(i%400==0):
                 print(i,"is leap year")
              else:
                 print(i,"is not leap year")
           else:
              print(i,"is leap year")
        else:
          print(i,"is not leap year")
yr = [2023,2024,1800,1900,2000,2003,2100,2200]
leapyear(yr)