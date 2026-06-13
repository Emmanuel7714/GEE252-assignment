import os

# =====================================================================
# Problem 1: Variables and Data Types
# =====================================================================
print("=== Problem 1 ===")

# 1. [span_8](start_span)Create variables with specified data types[span_8](end_span)
market_name = "Balogun Market"
num_traders = 5000
location_coords = (6.4541, 3.3947)
is_open_sundays = False

# 2. [span_9](start_span)Print each variable along with its data type using type()[span_9](end_span)
print(f"Market: {market_name}, Type: {type(market_name)}")
print(f"Traders: {num_traders}, Type: {type(num_traders)}")
print(f"Coordinates: {location_coords}, Type: {type(location_coords)}")
print(f"Open Sundays: {is_open_sundays}, Type: {type(is_open_sundays)}")

# 3. [span_10](start_span)Calculate and print average daily revenue per trader[span_10](end_span)
# Total market daily revenue = 25,000,000 Naira
total_daily_revenue = 25000000
avg_revenue_per_trader = total_daily_revenue / num_traders
print(f"Average Daily Revenue per Trader: {avg_revenue_per_trader} Naira")


# =====================================================================
# Problem 2: Lists and Basic Operations
# =====================================================================
print("\n=== Problem 2 ===")

host_countries = ["Ghana", "Egypt", "Nigeria", "Senegal", "Cameroon"]

# 4. [span_11](start_span)Add "Ivory Coast" to the end of the list[span_11](end_span)
host_countries.append("Ivory Coast")

# 5. [span_12](start_span)Insert "Morocco" at position 1[span_12](end_span)
host_countries.insert(1, "Morocco")

# 6. [span_13](start_span)Remove "Senegal" from the list[span_13](end_span)
host_countries.remove("Senegal")

# 7. [span_14](start_span)Print the total number of countries in the list[span_14](end_span)
print(f"Total number of countries: {len(host_countries)}")

# 8. [span_15](start_span)Print countries in alphabetical order without modifying original list[span_15](end_span)
print(f"Alphabetical order: {sorted(host_countries)}")

# 9. [span_16](start_span)Print every second country in the list using slicing[span_16](end_span)
print(f"Every second country: {host_countries[::2]}")


# =====================================================================
# Problem 3: Dictionaries
# =====================================================================
print("\n=== Problem 3 ===")

# [span_17](start_span)Initializing the base dictionary with the provided river data[span_17](end_span)
river_data = {
    "Nile": {"length_km": 6650, "countries": 11},
    "Congo": {"length_km": 4700, "countries": 9},
    "Niger": {"length_km": 4180, "countries": 5}
}

# 10. [span_18](start_span)Add a new river: "Zambezi"[span_18](end_span)
river_data["Zambezi"] = {"length_km": 2574, "countries": 6}

# 11. [span_19](start_span)Update Niger river's countries value to 6[span_19](end_span)
river_data["Niger"]["countries"] = 6

# 12. [span_20](start_span)Print all river names[span_20](end_span)
print("River names:", list(river_data.keys()))

# 13. [span_21](start_span)Print the number of countries the Congo river flows through[span_21](end_span)
print(f"Congo river flows through: {river_data['Congo']['countries']} countries")

# 14. [span_22](start_span)Calculate and print total combined length of all rivers[span_22](end_span)
total_length = sum(river['length_km'] for river in river_data.values())
print(f"Total combined length of all rivers: {total_length} km")


# =====================================================================
# Problem 4: Loops
# =====================================================================
print("\n=== Problem 4 ===")

print("--- Part A: For Loops ---")
# 15. [span_23](start_span)Multiplication table of 7 (from 7x1 to 7x10)[span_23](end_span)
print("Multiplication table of 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# 16. [span_24](start_span)Print each letter in the word "AFRICA"[span_24](end_span)
print("Letters in AFRICA:")
for letter in "AFRICA":
    print(letter)

# 17. [span_25](start_span)Sum of all even numbers from 1 to 50[span_25](end_span)
even_sum = 0
for num in range(1, 51):
    if num % 2 == 0:
        even_sum += num
print(f"Sum of even numbers from 1 to 50: {even_sum}")

print("\n--- Part B: While Loop ---")
# 18. [span_26](start_span)Count down from 20 to 1 and print[span_26](end_span)
print("Countdown:")
countdown = 20
while countdown >= 1:
    print(countdown, end=" " if countdown > 1 else "\n")
    countdown -= 1

# 19. [span_27](start_span)First number greater than 500 divisible by both 3 and 7[span_27](end_span)
number = 501
while True:
    if number % 3 == 0 and number % 7 == 0:
        print(f"First number > 500 divisible by 3 and 7 is: {number}")
        break
    number += 1


# =====================================================================
# Problem 5: Conditional Statements
# =====================================================================
print("\n=== Problem 5 ===")

# [span_28](start_span)Function to classify rainfall levels based on mm thresholds[span_28](end_span)
def classify_rainfall(mm):
    if mm > 300:
        return "Flood Risk"
    elif 200 <= mm <= 300:
        return "Heavy Rain"
    elif 100 <= mm <= 199:
        return "Moderate Rain"
    elif 1 <= mm <= 99:
        [span_29](start_span)return "Light Rain"[span_29](end_span)
    elif mm == 0:
        return "Dry"
    else:
        return "Invalid Input"

# [span_30](start_span)Test your function with: 350, 250, 150, 50, 0[span_30](end_span)
test_rainfall_values = [350, 250, 150, 50, 0]
print("Rainfall Classification Results:")
for value in test_rainfall_values:
    print(f"{value}mm: {classify_rainfall(value)}")


# =====================================================================
# Problem 6: Functions
# =====================================================================
print("\n=== Problem 6 ===")

print("--- Part A: Basic Function ---")
# [span_31](start_span)Function converts USD to NGN[span_31](end_span)
def calculate_exchange(amount, rate):
    return amount * rate

# [span_32](start_span)Test calculation[span_32](end_span)
usd_amount = 100
exchange_rate = 1580
converted_result = calculate_exchange(usd_amount, exchange_rate)
print(f"Exchange Result: {converted_result}")


print("\n--- Part B: Function with Default Parameters ---")
# [span_33](start_span)Function formats price with comma separators and currency strings[span_33](end_span)
def format_price(amount, currency="NGN"):
    return f"{currency} {amount:,}"

# [span_34](start_span)Run required test cases[span_34](end_span)
print(format_price(5000))
print(format_price(200, "GHS"))


print("\n--- Part C: Function Returning Multiple Values ---")
# [span_35](start_span)Function returns min, max, and calculated mean of a score list[span_35](end_span)
def analyze_scores(scores):
    lowest = min(scores)
    highest = max(scores)
    average = sum(scores) / len(scores)
    return lowest, highest, average

# [span_36](start_span)Run required test case[span_36](end_span)
score_list = [55, 72, 88, 61, 94, 47, 79]
lowest_score, highest_score, class_avg = analyze_scores(score_list)
print(f"Test Scores List: {score_list}")
print(f"Lowest Score: {lowest_score}")
print(f"Highest Score: {highest_score}")
print(f"Class Average: {class_avg:.2f}")


# =====================================================================
# Problem 7: String Operations
# =====================================================================
print("\n=== Problem 7 ===")

proverb = "Slowly, slowly, catches the monkey, African wisdom"

# 20. [span_37](start_span)Convert string to uppercase[span_37](end_span)
print(f"Uppercase: {proverb.upper()}")

# 21. [span_38](start_span)Split into a list using comma as separator[span_38](end_span)
split_proverb = proverb.split(",")
print(f"Split List: {split_proverb}")

# 22. [span_39](start_span)Check whether the string contains the word "wisdom"[span_39](end_span)
contains_wisdom = "wisdom" in proverb
print(f"Contains 'wisdom': {contains_wisdom}")

# 23. [span_40](start_span)Replace "African wisdom" with "African proverb"[span_40](end_span)
new_proverb = proverb.replace("African wisdom", "African proverb")
print(f"Replaced: {new_proverb}")

# 24. [span_41](start_span)Count how many times the letter 'o' appears (case-insensitive)[span_41](end_span)
o_count = proverb.lower().count('o')
print(f"Count of 'o': {o_count}")


# =====================================================================
# Problem 8: File Operations
# =====================================================================
print("\n=== Problem 8 ===")

filename = "crops.txt"

# 25. [span_42](start_span)Create file called crops.txt with structured data content[span_42](end_span)
file_content = """Cocoa, Nigeria, 320000
Coffee, Ethiopia, 480000
Cassava, Ghana, 210000"""

with open(filename, "w") as file:
    file.write(file_content)
print(f"'{filename}' created successfully.")

# [span_43](start_span)26, 27, 28. Read, process production metrics, and handle exceptions[span_43](end_span)
try:
    total_production = 0
    print(f"\nReading lines from {filename}:")
    
    with open(filename, "r") as file:
        for line in file:
            stripped_line = line.strip()
            [span_44](start_span)print(stripped_line)  # Print each line[span_44](end_span)
            
            # Process string structural items to extract annual production values
            parts = stripped_line.split(",")
            if len(parts) == 3:
                annual_tonnes = int(parts[2].strip())
                total_production += annual_tonnes
                
    print(f"\nTotal annual production across all crops: {total_production} tonnes")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except ValueError:
    print("Error: Could not convert numeric database item from file data.")
finally:
    # Cleanup file afterward to keep space neat
    if os.path.exists(filename):
        os.remove(filename)


# =====================================================================
# Problem 9: List Comprehensions
# =====================================================================
print("\n=== Problem 9 ===")

temperatures = [18, 23, 31, 27, 35, 19, 29, 33, 22, 28]

# 29. [span_45](start_span)List of temperatures converted to Fahrenheit: F = (C * 9/5) + 32[span_45](end_span)
fahrenheit_temps = [(c * 9/5) + 32 for c in temperatures]
print(f"Fahrenheit Conversion: {fahrenheit_temps}")

# 30. [span_46](start_span)List of only temperatures above 30 degrees Celsius[span_46](end_span)
above_30_temps = [c for c in temperatures if c > 30]
print(f"Temperatures > 30°C: {above_30_temps}")

# 31. [span_47](start_span)List of temperatures rounded to nearest whole number between 20 and 29 inclusive[span_47](end_span)
filtered_range_temps = [round(c) for c in temperatures if 20 <= c <= 29]
print(f"Rounded temperatures between 20 and 29: {filtered_range_temps}")


# =====================================================================
# Problem 10: Error Handling
# =====================================================================
print("\n=== Problem 10 ===")

def run_bank_transaction():
    try:
        # 32. [span_48](start_span)Ask user to input parameters[span_48](end_span)
        # Using manual string mock configurations for autonomous script testing
        # To make it fully interactive, change assignment to: input("Enter account balance: ")
        print("(Simulated Inputs: Balance = 50000, Withdrawal = 75000)")
        input_balance = "50000"
        input_withdrawal = "75000"
        
        balance = float(input_balance)
        withdrawal = float(input_withdrawal)
        
        # 34. [span_49](start_span)Custom logical restriction check for balance caps[span_49](end_span)
        if withdrawal > balance:
            print("Error: Insufficient funds!")
            [span_50](start_span)print("You cannot withdraw more than your balance.")[span_50](end_span)
        else:
            # 33. [span_51](start_span)Calculate and print remaining balance[span_51](end_span)
            remaining_balance = balance - withdrawal
            print(f"Transaction successful! Remaining balance: {remaining_balance}")
            
    except ValueError:
        # [span_52](start_span)Handle cases where inputs cannot be cast cleanly to numeric formats[span_52](end_span)
        print("Error: Invalid input! Balance and withdrawal must be valid numbers.")
        
    finally:
        # 35. [span_53](start_span)This statement evaluates regardless of internal operation success[span_53](end_span)
        print("Transaction attempt completed")

# Execute transactional sequence demonstration
run_bank_transaction()