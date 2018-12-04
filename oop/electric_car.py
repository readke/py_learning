from Car import Car

class ElectricCar(Car):

    def __init__(self,make,model,year):
        #初始化父类属性
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a "+ str(self.battery_size) + " -kWh battery.")

    def read_odometer(self):
        print("100")

my_tesla = ElectricCar('tesla' ,'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.read_odometer()
