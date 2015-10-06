import tempconv, os

def clear():
    os.system('clear')

def incorrect():
    print("You have selected an incorrect number. Please select again.")

def choice():
    x = int(input("What is your unknown? "))
    return x

def xagain():
    input("Press enter to do another conversion.")

def menu():
    clear()
    print("""
    Gas Law Conversions
    
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

def pressureVolume():
    clear()
    print("""
    Pressure and Volume
    
    """)
    print("""
    Unknown:
    
    1. Pressure
    2. Volume
    """)
    z = choice()
    if z == 1:
        pressureVolumePressure()
    elif z == 2:
        pressureVolumeVolume()
    else:
        incorrect()
        pressureVolume()

def pressureVolumePressure():
    clear()
    print("Unknown Pressure")
    P1 = int(input("P1= "))
    V1 = int(input("V1= "))
    V2 = int(input("V2= "))
    P2 = (P1 * V1) / V2
    print()
    print("P2= " + str(P2))
    xagain()
    menu()

def pressureVolumeVolume():
    clear()
    print("Unknown Volume")
    P1 = int(input("P1= "))
    V1 = int(input("V1= "))
    P2 = int(input("V2= "))
    V2 = (P1 * V1) / P2
    print()
    print("V2= " + str(V2))
    input("Press enter to do another conversion.")
    menu()

def volumeTemperature():
    clear()
    print("Volume and Temperature")
    print()
    print("""
    Unknown:
            
    1. Temperature
    2. Volume
    """)
    z = choice()
    if z == 1:
        volumeTemperatureTemperature()
    elif z == 2:
        volumeTemperatureVolume()
    else:
        incorrect()
        volumeTemperature()

def volumeTemperatureTemperature():
    clear()
    print("Unknown Temperature")
    V1 = int(input("V1= "))
    T1t = int(input("T1= "))
    print("""
    1. Kelvin
    2. Celsius
    3. Fahrenheit
    """)
    tempChoice = int(input("What are the units for T1? "))
    if tempChoice == 1:
        T1 = tempconv.xkelvin(T1t)
    elif tempChoice == 2:
        T1 = tempconv.xcelcius(T1t)
    elif tempChoice == 3:
        T1 = tempconv.xfahrenheit(T1t)
    else:
        incorrect()
        input()
        volumeTemperatureTemperature()
    V2 = int(input("V2= "))
    T2 = V2 / (V1 / T1)
    tempconv.xkelvin(T2)
    xagain()
    menu()

def volumeTemperatureVolume():
    clear()
    print("Unknown Volume")
    V1 = int(input("V1= "))
    T1t = int(input("T1= "))
    print("""
        1. Kelvin
        2. Celsius
        3. Fahrenheit
        """)
    tempChoice = int(input("What are the units for T1? "))
    if tempChoice == 1:
        T1 = tempconv.xkelvin(T1t)
    elif tempChoice == 2:
        T1 = tempconv.xcelcius(T1t)
    elif tempChoice == 3:
        T1 = tempconv.xfahrenheit(T1t)
    else:
        incorrect()
        input()
        volumeTemperatureVolume()
    T2t = int(input("T1= "))
    print("""
        1. Kelvin
        2. Celsius
        3. Fahrenheit
        """)
    tempChoice = int(input("What are the units for T1? "))
    if tempChoice == 1:
        T2 = tempconv.xkelvin(T2t)
    elif tempChoice == 2:
        T2 = tempconv.xcelcius(T2t)
    elif tempChoice == 3:
        T2 = tempconv.xfahrenheit(T2t)
    else:
        incorrect()
        input()
        volumeTemperatureVolume()
    V2 = (V1 / T1) * T2
    print("V2= " + str(V2))
    xagain()
    menu()

#def pressureTemperature():


#def volumeN():


#def pressureVolumeTemperature():


#def PVEqualsNRT():


#def rateMass():


def main():
    menu()

if __name__ == '__main__':
    main()






