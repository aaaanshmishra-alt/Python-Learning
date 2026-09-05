#write a function to convert celsius to farenheit and vice versa
def temprature_converter(temperature, unit):
    if unit == "c":
        print("farenheit", "=", temperature * 9 / 5 + 32)
    elif unit == "f":
        print("celsius", "=", (temperature - 32 )* 5/9)
temprature_converter(25,"c")
    