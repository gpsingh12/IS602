class CarEvaluation(object):
    """Car Evaluation class"""
    carCount = 0
    def __init__(self, Brand, Price, Safety_Rating):
        """Constructor function for class
        Attributes:
        Brand(str): brand name of car
        Price(str): price of car
        Safety_Rating(str): safety rationg of car
        """
        
        self.Brand = Brand
        self.Price = Price
        self.Safety_Rating = Safety_Rating
        CarEvaluation.carCount +=1

    def showEvaluation(self):
        """method to print out the car brasnd names and their features"""
        
        print "The %s has a %s price and it's safety is rated %s" %(self.Brand, self.Price, self.Safety_Rating)

def sortbyprice(List, order):
    """Method to sort the cars by price
    Arg:
    List(list): list of cars
    order(str): ascending or descending as input
    Return:
    return the lisat of car names in sorted order of their price
    """
    sortedlist = []
    asclist = ["Low", "Med", "High"]
    dsclist = ["High", "Med", "Low"]
    
    if order == "asc":
        for carprice in asclist:
            for car in List:
                if car.Price == carprice:
                    sortedlist.append(car.Brand)
    else:
        for carprice in dsclist:
            for car in List:
                if car.Price == carprice:
                    sortedlist.append(car.Brand)
    return sortedlist
        
def searchforsafety(List, search_val):
     """ The method search_val in rating and return True or False
        Arg:
        List(list): list of carevaluation objects
        s_rating(int): integer value for user input
        Return:
        returns True or False depending if value is contained in List
        """
     for car in List:
        if car.Safety_Rating == search_val:
            return True
     else:
            return False
            



if __name__ == "__main__":	
   eval1 = CarEvaluation("Ford", "High", 2)
   eval2 = CarEvaluation("GMC", "Med", 4)
   eval3 = CarEvaluation("Toyota", "Low", 3)

   print "Car Count = %d" % CarEvaluation.carCount # Car Count = 3

   eval1.showEvaluation() #The Ford has a High price and it's safety is rated a 2
   eval2.showEvaluation() #The GMC has a Med price and it's safety is rated a 4
   eval3.showEvaluation() #The Toyota has a Low price and it's safety is rated a 3

   L = [eval1, eval2, eval3]

   print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]
   print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
   print searchforsafety(L, 2); #true
   print searchforsafety(L, 1); #false
