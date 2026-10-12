def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def wind_chill(temp, wind_speed):
    return 35.74 + (0.6215 * temp) - (35.75 * wind_speed ** 0.16) + (0.4275 * temp * wind_speed ** 0.16)

def main():
    temp = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").upper()
    if unit == "C":
        temp = celsius_to_fahrenheit(temp)

    for speed in range(5, 61, 5):
        chill = wind_chill(temp, speed)
        print(f"At temperature {temp:.1f}F, and wind speed {speed} mph, the windchill is: {chill:.2f}F")

main()