"""Unreliablecar class test"""


from unreliable_car import UnreliableCar





def main():

    """Test some UnreliableCars."""



    # cars with different reliabilities

    good_car = UnreliableCar("Mostly Good", 100, 90)

    bad_car = UnreliableCar("Dodgy", 100, 9)



    # attempt to drive the cars many times

    # output based on the driven distance

    for i in range(1, 12):

        print("Attempting to drive {}km:".format(i))

        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))

        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))



    # Final stage of car

    print(good_car)

    print(bad_car)

main()