def calculate_turbine_power(power_demand):
    turbine_power = (power_demand / 2) + 12
    return turbine_power

while True:
    user_input = input("Enter power demand (or 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Exiting program.")
        break
    try:
        power_demand = float(user_input)
        turbine_power = calculate_turbine_power(power_demand)
        print("Turbine needed:", turbine_power)
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")