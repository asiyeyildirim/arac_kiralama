###### parent class ######

class VehicleRent:
    def __init__(self, stock):
        pass

    def displayStock(self):
     """ 
     display stock
     """
    pass
  
    def rentHourly(self,n):
         """ 
     rent hourly
     """
    pass

    def rentDaily(self,n):
         """ 
     rent daily
     """
    pass

    def returnVehicle(self,request,brand):
         """ 
     return a  bill
     """
    pass


   #### child class 1 ####

class CarRent(VehicleRent):

    def __init__(self):
       pass

    def discount():
       pass

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
