import tempconv

def menu():
    print("""
        1. Pressure and Volume
        2. Volume and Temperature
        3. Pressure and Temperature
        4. Volume and n
        5. Pressure, Volume, and Temperature
        6. PV=nRT
        7. Rate and Mass
        8. Quit
        """)
        mc = (int(input("What would you like to do? Please enter a number: ")))
        if mc == 1:
            pressureVolume()
        elif mc == 2:
            volumeTemperature()
        elif mc == 3:
            pressureTemperature()
        elif mc == 4:
            volumeN()
        elif mc == 5:
            pressureVolumeTemperature()
        elif mc == 6:
            PVEqualsNRT()
        elif mc == 7:
            rateMass()
        elif mc == 8:
            print("Quitting...")
            exit()
        else:
            print("That was not one of the options, please make another choice.")
            wait = input("Please press enter to continue.")
            menu()

def main():
    menu()

if __name__ == '__main__':
    main()

def pressureVolume():


def volumeTemperature():


def pressureTemperature():


def volumeN():


def pressureVolumeTemperature():


def PVEqualsNRT():


def rateMass():