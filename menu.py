
class Data():
    bike_prices = [1000, 2000, 3000, 4000, 5000, 6000]
    bike_number = ['001', "002", "003", "004", "005", "006"]
    bike_weight = ["100kgs", "200kgs", "300kgs", "400kgs", "500kgs", "600kgs"]
    bike_names = ["CLASSIC", "BULLET", "THUNDERBIRD", "INTERCEPTOR", "INTERCEPTOR", "HIMALAYAN"]
  
class Marketer(Data):
    cost=0
    o=0
    def __init__(self):
        print('created')

    def print_menu(self):
        print("BIKE MENU")
        for i in range(len(Data.bike_names)):
            print(i+1,Data.bike_names[i],sep=':')
            


    def print_details(self,name):
        print("{:<8} {:<8} {:<8} {:<8}".format("NAME","NUMBER","WEIGHT","PRICE"))
        
        for i in range(len(Data.bike_names)):
            
            if name== Data.bike_names[i]:
                
                
                print("{:<8} {:<8} {:<8} {:<8}".format(Data.bike_names[i],Data.bike_number[i],Data.bike_weight[i],Data.bike_prices[i]))
            if name==Data.bike_names[i]:
                
                
              
                self.o=Data.bike_prices[i]
                self.cost = self.cost + self.o
                
                

                
            

class User():
    
    def take_input(self):
        
            print('please select bike u like')
            name_of_bike=input()
            return name_of_bike
        


ob=Marketer()
ob.print_menu()
name='p'
while name!= 'STOP':
    

    name=User().take_input().upper()
    
    if name=='STOP':
        print('thank you visit again')
    else:
        ob.print_details(name)

    


print('bill=',ob.cost)

   


