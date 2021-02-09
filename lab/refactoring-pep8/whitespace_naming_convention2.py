# By Kami Bigdely
# PEP8 - whitespaces and variable names.
class Pizza:
    def __init__ (self, bread_type, cheese_type, meat_type, pizza_toppings, size):
        self.bread = bread_type
        self.cheese = cheese_type
        self.meat = meat_type
        self.toppings = pizza_toppings
        self.size = size        
    @classmethod
    def Create_ChicagoPizza (cls, class_type, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meat= 'Italian sausage'
        toppings = ['green bell pepper','mushroom', 'chunky tomato sauce', 'onion']
        return class_type (bread, cheese, meat, toppings, size)   
    @classmethod
    def create_California_pizza(cls, class_type, meat, size):
        bread = 'thin crust'
        cheese = 'feta cheese'
        toppings =[ 'garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper' ]
        return cls(bread, cheese, meat, toppings, size) 
    def print_Info(self):
        print('bread type is: ', self.bread)
        print('cheese type is: ', self.cheese)
        print('meat type is: ', self.meat)
        print('Toppings are: ', end='')
        print(', '.join(map(str, self.toppings)))
myPizza = Pizza.create_California_pizza(Pizza, 'chicken', 'large')
myPizza.print_Info()