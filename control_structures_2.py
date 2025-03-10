#inputs the temp in farenheit and converts it into celcius
#displays both temp using appro format

initial_temp = int(input("What is the current temp in Fahrenheit: "))

celcius = round((initial_temp-32)/(9/5))

print(f"The temparature in celcius is {celcius}")

