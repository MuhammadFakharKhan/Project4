# Gravitational constants for each planet as a percentage of Earth's gravity


planet_gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Prompt the user to enter their weight on Earth
earth_weight = float(input("Enter your weight on Earth (in kg): "))

# Prompt the user to enter the name of a planet
planet_name = input("Enter the name of a planet in our solar system: ")

# Check if the planet is in the dictionary
if planet_name in planet_gravity:
    # Calculate the weight on the specified planet
    planet_weight = earth_weight * planet_gravity[planet_name]
    # Print the result rounded to 2 decimal places
    print(f"Your weight on {planet_name} would be {round(planet_weight, 2)} kg.")
else:
    # Handle the case where the planet name is invalid
    print("Invalid planet name. Please enter a valid planet from the solar system.")

