import datetime
###### parent class ######

class VehicleRent:
    def __init__(self, stock):
        self.stock=stock
        self.now=0 #fatura hesaplarken kullanacağız 

    def displayStock(self):
     """ 
     display stock
     """
     print("{} vehicle avaliable to rent".format(self.stock))  #kiralanabilir kaç araç var, sayısını verir
     return self.stock
  
    def rentHourly(self,n): #n=müşteri tarafından kiralanan araç sayısı
         """ 
     rent hourly
     """
         if n<=0:
          print("Number should be positive")
          return None
     
         elif n>self.stock:
            print("Sorry{} vehicle available to rent".format(self.stock))
            return None
         else:
           self.now=datetime.datetime.now()
           print("Rented a {} vehicle for hourly at {} hours".format(n,self.now))

           self.stock -=n #garajda bulunan araç sayısından; müşteririnin istediği araç sayısını çıkart

           return self.now #saat farkına göre ödenmesi gereken faturayı belirlemek için


    def rentDaily(self,n):
         """ 
     rent daily
     """
         if n<=0:
             print("Number should be positive")
             return None

         elif n>self.stock:
            print("Sorry{} vehicle available to rent".format(self.stock))
            return None

         else:
           self.now=datetime.datetime.now()
           print("Rented a {} vehicle for daily at {} hours".format(n,self.now))

           self.stock -=n #garajda bulunan araç sayısından; müşteririnin istediği araç sayısını çıkart

           return self.now #saat farkına göre ödenmesi gereken faturayı belirlemek için


    def returnVehicle(self,request,brand):
         """ 
     return a  bill
     """
         car_h_price=10
         car_d_price=car_h_price*8/10*24
         bike_h_price=5
         bike_d_price=bike_h_price*7/10*24

         rentalTime, rentalBasis, numOfVehicle = request
         bill=0

         if brand=="car":
             if rentalTime and rentalBasis and numOfVehicle:
                 self.stock += numOfVehicle
                 now=datetime.datetime.now()
                 rentalPeriod = now- rentalTime

                 if rentalBasis == 1: #hourly
                     bill =rentalPeriod.second/3600*car_h_price*numOfVehicle

                 elif rentalBasis == 2: #daily
                     bill =rentalPeriod.second/(3600*24)*car_d_price*numOfVehicle
 
                 if(2 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill= bill*0.8

                 print("Thank you for returning your car")
                 print("Price: $ {}".format(bill))
                 return bill


         elif brand=="bike":
             if rentalTime and rentalBasis and numOfVehicle:
                 self.stock += numOfVehicle
                 now=datetime.datetime.now()
                 rentalPeriod = now- rentalTime

                 if rentalBasis == 1: #hourly
                     bill =rentalPeriod.second/3600*bike_h_price*numOfVehicle

                 elif rentalBasis == 2: #daily
                     bill =rentalPeriod.second/(3600*24)*bike_d_price*numOfVehicle
 
                 if(4 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill= bill*0.8

                 print("Thank you for returning your bike")
                 print("Price: $ {}".format(bill))
                 return bill
         else:
            print("You don't rent a vehicle")
            return None


   #### child class 1 ####

class CarRent(VehicleRent):

    global discount_rate
    discount_rate=15

    def __init__(self,stock):
        super().__init__(stock)


    def discount(self,b):
       bill= b- (b*discount_rate)/100
       return bill

    #### child class 2 ####

class BikeRent(VehicleRent):
      
     def __init__(self):
       pass

#Customer

class Customer:

     def __init__(self):
       pass
    
     def requestVehicle():

          """ 
         request vehicle
     """
     pass

     def returnVehicle():

          """ 
     return vehicle
     """
     pass
