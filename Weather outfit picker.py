temperature = int(input("Enter the temperature in celcius :"))

if temperature < 20:
    outfit = "jacket"
    print("It is cold today")
    print("wear a oufit :" , outfit)
else:
    outfit = "T-shirt"
    print("It is hot today")
    print("wear a " , outfit)

is_raining = input("Is it raining today? (yes/no)")
print("take an umbrella")

wind_speed = int(input("enter the wind sppped in km/hr :"))

if wind_speed > 30:
    need_windbreaker = "yes"
    print("It is windy today")
    print("Wear a windbreaker over your" , outfit)
else:
    need_windbreaker = "no"
    print("It is calm today")
    print("No windbreaker over your " , outfit)

has_puddles = input("Are there puddles on ground? (yes/no)")

if has_puddles == "yes":
    shoes = ("boots")
    print("Ground is wet")
    print("wear" , shoes)
else:
    shoes = "sneakers"
    print("It is dry today")
    print("wear" , shoes)

print("")
print("Weather check complete")

print("=====Weather Outfit Picker=====")
print("Temperature:" , temperature)
print("Outfit chosen:" , outfit)
print("Raining:" , is_raining)
print("Windbreaker:" , need_windbreaker)
print("Shoes Chosen:" , shoes)
print("===========================")
