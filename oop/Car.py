class Car():
    """一次模拟汽车的简单尝试"""
   
    def __init__(self,make,model,year):
        #初始化汽车属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        #返回整洁的描述信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def read_odometer(self):
        #打印一条指出汽车里程的消息
        print("this car has " + str(self.odometer_reading) + " miles on it.")

    def set_odometer(self,mileage):
        #禁止任何人回调里程数
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self,miles):
        if miles < 0 :
            print("you can't set this odometer")
        else :
            self.odometer_reading += miles
'''
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.set_odometer(23)
my_new_car.set_odometer(12)
my_new_car.read_odometer()
''' 

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