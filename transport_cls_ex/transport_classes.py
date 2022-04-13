import random
import time
from abc import ABC, abstractmethod


class Transport(ABC):
    """Abstract class for transport implementation."""
    transport_type = "vehicles"
    _fuel_quantity = 0
    _speed_at_the_moment = 0
    _is_public = False

    def __init__(self, mark: str, brand: str, max_speed: int,
                 fuel_tank_capacity: int, seats_numb: int):
        """Magic method for transport initialization."""
        self.mark = mark
        self.brand = brand
        self.max_speed = max_speed
        self.fuel_tank_capacity = fuel_tank_capacity
        self.seats_numb = seats_numb

    def check_fuel_level(self):
        """Method which shows up fuel level as relation fuel_level to fuel tank capacity."""
        print(f"fuel level is {int(self._fuel_quantity)}/{self.fuel_tank_capacity}")

    def get_diff_fuel_level(self):
        """The method returns difference between tank capacity and fuel quantity.
        This method is auxiliary to the add_fuel method.
        """
        return self.fuel_tank_capacity - self._fuel_quantity

    def add_fuel(self, number_of_liters: int):
        """The method allows refuel the transport."""
        diff = self.get_diff_fuel_level()
        if number_of_liters <= diff:
            self._fuel_quantity += number_of_liters
            self.check_fuel_level()
        if number_of_liters > diff:
            self._fuel_quantity += diff
            print(f"Sorry, the tank cannot take that much fuel {number_of_liters}\n"
                  f"{diff} liters of fuel were refueled")

    def decrease_fuel(self, numb_for_decr: int):
        """The method allows decrease the fuel level in the transport."""
        self._fuel_quantity -= numb_for_decr

    @abstractmethod
    def start_moving(self):
        """This is an abstract method that will be used in subsequent classes.
        It implements the transport moving logic
        """

    @abstractmethod
    def stop_moving(self):
        """This is an abstract method that will be used in the following classes.
        It implements the logic of stopping transport
        """
    @property
    def speed_at_the_moment(self):
        """The method returns transport current speed."""
        return f"The current speed is {self._speed_at_the_moment} km/h"

    @speed_at_the_moment.setter
    def speed_at_the_moment(self, speed_value: int):
        """The method sets transport current speed."""
        self._speed_at_the_moment = speed_value

    @property
    def is_public(self):
        """The method return is_public value"""
        return self._is_public

    @is_public.setter
    def is_public(self, new_status: bool):
        """The method return is_public value"""
        if isinstance(new_status, bool):
            return self._is_public
        raise ValueError("The value must be of boolean type")

    def fuel_vs_distance(self, time_on_the_way: int, get_fuel_per_hundred_km: int):
        """TThe method allows you to check whether there is enough fuel
        to travel the specified distance."""
        passed_distance = (time_on_the_way / 60) * self._speed_at_the_moment
        fuel_consumption = (passed_distance * get_fuel_per_hundred_km) / 100
        if fuel_consumption > self._fuel_quantity:
            return False
        return fuel_consumption

    def moving_process(self, engine_status: bool, get_fuel_per_hundred_km: int):
        """The method provides transport moving logic"""
        while engine_status and self._fuel_quantity > 0:
            time_on_the_way = random.randint(1, 20)
            self.speed_at_the_moment = random.randint(1, self.max_speed)
            fuel_check = self.fuel_vs_distance(time_on_the_way, get_fuel_per_hundred_km)
            if not fuel_check:
                can_pass_dist = (self._fuel_quantity * 100) / get_fuel_per_hundred_km
                drive_time_left = can_pass_dist / self._speed_at_the_moment
                time.sleep(drive_time_left)
                self._fuel_quantity = 0
                self.stop_moving()
                print("We spent all gasoline")
            else:
                print(self.speed_at_the_moment)
                time.sleep(time_on_the_way)
                self.decrease_fuel(fuel_check)
                self.check_fuel_level()

    def __add__(self, other):
        """The method is reloaded for adding fuel to tank."""
        self.add_fuel(other)

    def __del__(self):
        """The method is reloaded to have the class name of deleted object."""
        return f"The object of {self.__class__.__name__} was deleted"

    def __dir__(self):
        """Please, do not touch it!."""
        return "Та просто розкрий клас та подивись на ті методи і не чіпай мене, будь-ласка!"


class Engine:
    """The Engine class for initializing engine.
    The class is used to implement several engine functions in the subsequent classes."""
    _is_working = False

    def __init__(self, power, eng_displacement, get_fuel_per_hundred_km):
        """Magic method for transport initialization."""
        self.power = power
        self.eng_displacement = eng_displacement
        self.get_fuel_per_hundred_km = get_fuel_per_hundred_km

    @property
    def engine_status(self):
        """The method checks the class attribute 'is_working'.
        The engine is working if the method returns True
        and doesn't if it returns False.
        """
        if self._is_working:
            print(f"Engine is working")
            return True
        print(f"Engine is stopped")
        return False

    @engine_status.setter
    def engine_status(self, new_status):
        """The method allows setting the value of the "is_working" attribute."""
        self._is_working = new_status

    def __gt__(self, other):
        """The method is reloaded for comprising the engines power."""
        return self.power > other.power

    def __lt__(self, other):
        """The method is reloaded for comprising the engines power."""
        return self.power < other.power


class Car(Transport, Engine):
    """The car class for initializing car instances"""
    def __init__(self, mark: str, brand: str,
                 max_speed: int, fuel_tank_capacity: int,
                 seats_numb: int, power: int, eng_displacement: int,
                 get_fuel_per_hundred_km: int):
        """Magic method for car initialization."""
        Transport.__init__(self, mark, brand, max_speed, fuel_tank_capacity, seats_numb)
        Engine.__init__(self, power, eng_displacement, get_fuel_per_hundred_km)

    def stop_moving(self):
        """The implemented abstract method of Transport class.
        The method allows turn off the engine_status to False and stop moving.
        """
        self.engine_status = False

    def start_moving(self):
        """The implemented abstract method of Transport class.
        The method allows you to turn on engine_status to True and start moving.
        """
        self.engine_status = True
        self.moving_process(self._is_working, self.get_fuel_per_hundred_km)


class Bus(Transport, Engine):
    """The bus class for initializing car instances"""
    _is_public = True

    def __init__(self, mark: str, brand: str,
                 max_speed: int, fuel_tank_capacity: int,
                 seats_numb: int, power: int,
                 eng_displacement: int, get_fuel_per_hundred_km: int):
        """Magic method for bus initialization."""
        Transport.__init__(self, mark, brand, max_speed, fuel_tank_capacity, seats_numb)
        Engine.__init__(self, power, eng_displacement, get_fuel_per_hundred_km)

    def stop_moving(self):
        """The implemented abstract method of Transport class.
        The method allows turn off the engine_status to False and stop moving.
        """
        self.engine_status = False

    def start_moving(self):
        """The implemented abstract method of Transport class.
        The method allows you to turn on engine_status to True and start moving.
        """
        self.engine_status = True
        self.moving_process(self._is_working, self.get_fuel_per_hundred_km)


class Boat(Transport, Engine):
    """The boat class for initializing car instances"""
    transport_type = "water"
    _is_public = True

    def __init__(self, mark: str, brand: str, max_speed: int,
                 fuel_tank_capacity: int, seats_numb: int,
                 power: int, eng_displacement: int,
                 get_fuel_per_hundred_km: int, boat_type: str):
        """Magic method for bus initialization."""
        Transport.__init__(self, mark, brand, max_speed, fuel_tank_capacity, seats_numb)
        Engine.__init__(self, power, eng_displacement, get_fuel_per_hundred_km)
        self.boat_type = boat_type

    def stop_moving(self):
        """The implemented abstract method of Transport class.
        The method allows turn off the engine_status to False and stop moving.
        """
        self.engine_status = False

    def start_moving(self):
        """The implemented abstract method of Transport class.
        The method allows you to turn on engine_status to True and start moving.
        """
        self.engine_status = True
        self.moving_process(self._is_working, self.get_fuel_per_hundred_km)


if __name__ == "__main__":

    car = Car(mark="Mustang", brand="Ford", max_speed=300,
              fuel_tank_capacity=100, seats_numb=4, power=400,
              eng_displacement=5, get_fuel_per_hundred_km=15)
    car.add_fuel(80)

    bus = Bus(mark="ATF500", brand="Mercedes", max_speed=200,
              fuel_tank_capacity=500, seats_numb=50, power=200,
              eng_displacement=7, get_fuel_per_hundred_km=20)
    ferry = Boat(mark="SomeFerry", brand="BigBoat", max_speed=15,
                 fuel_tank_capacity=20000, seats_numb=4500, power=5000,
                 eng_displacement=7, get_fuel_per_hundred_km=700, boat_type='ferry')
    try:
        # print(car.__del__())
        print(car.__dir__())
        car.start_moving()
    except KeyboardInterrupt:
        car.stop_moving()
        print("The car was stopped")
