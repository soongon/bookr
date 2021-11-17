# 덧셈하는 함수
def add_two_numbers(num_one=0, num_two=0):
    return num_one + num_two


# 함수를 사용
result = add_two_numbers(3, 5)
print(result)

result2 = add_two_numbers(num_two=5)
print(result2)


class Car:
    brand = 'hyundai'
    cc = 2000
    price = 30000000

    def drive(self):
        pass


class SuperCar(Car):
    max_speed = 300

    def drive(self):
        print('매우 빠름')


ferrari = SuperCar()
print(ferrari.max_speed)

my_car = Car()
my_car.brand = 'kia'
print(my_car.brand)
