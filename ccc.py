print ("-----------------------------------------------")
print ("--------WELCOME WITH PYTHON CALCULATOR---------")
print ("-----------------------------------------------")

import os
import datetime
def bilcal():
    tot=0
    currentDate=datetime.date.today()
    print(currentDate.strftime("%d %B %Y"))
    while True:
        try:
            price=input("\nEnter Item Price:Rs ")
            tot=tot+price
            if not price:
                if not tot:
                    print("Error")
                    quit()
                break
            

        
            print("Total Price Is :Rs %.2f" % tot)
            
            dis = 0.05 * tot
            dis1 = 0.10 * tot
            dis2 = 0.12 * tot
            total = tot - dis
            total2 = tot - dis1
            total3 = tot - dis2

            
            print ("01) Total with 5% discount: Rs" + format( total, ",.2f"))
            print ("-----02) Total with 10% discount: Rs" + format( total2, ",.2f"))
            print ("----------03) Total with 12% discount: Rs" + format( total3, ",.2f"))

            
        except ValueError as e:
            print(e)
            break

     
    
    print("\n\tDiscount Price is :Rs %.2f" % tot1)          

              
bilcal()    
    

