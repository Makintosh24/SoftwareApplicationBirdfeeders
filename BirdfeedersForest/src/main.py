
# BirdfeedersForest app
#
# to start go to folder birdfeeders and type
#     python.exe .\src\main.py
#
# Copyright (c) by Shilyn Makin



import math

# Variable declarations

birdfeeders: int = 0  # Number of bird feeders in the forest of 5000 ha

# Calculated final survival rate based on diminishing returns formula
calculated_survival_rate: float = 0.0

# Forest attractiveness description
forestattractiveness: str = "The forest is considered more attractive due to the increased healthier bird population."


import math

# Variable declarations
birdfeeders: int = 0  # Number of bird feeders in the forest of 5000 ha
calculated_survival_rate: float = 0.0
forestattractiveness: str = "The forest is considered more attractive due to the increased healthier bird population."

# Function to classify bird feeders into segments and provide survival rate range
def classify_bird_feeders(feeders: int) -> tuple:
    if feeders < 1:
        return 'O', (0.0, 0.0)  # No feeders
    elif 1 <= feeders <= 3:
        return 'A', (0.1, 0.3)  # Segment A: Few feeders
    elif 4 <= feeders <= 6:
        return 'B', (0.3, 0.6)  # Segment B: Moderate feeders
    elif feeders >= 7:
        return 'C', (0.6, 0.99)  # Segment C: Many feeders

# Function to calculate survival rate with diminishing returns
def calculate_survival_rate_with_diminishing_returns(feeders: int, initial_rate: float) -> float:
    k = 0.38  # Scaling factor for feeders' impact
    survival_rate = initial_rate + math.log10(1 + k * feeders)
    return min(max(survival_rate, 0.1), 0.99)

# Function to determine forest attractiveness
def calculate_attractiveness_with_diminishing_returns(feeders: int, survival_rate: float) -> str:
    if feeders == 0 or survival_rate < 0.2:
        return "Not very attractive"
    elif 1 <= feeders <= 3:
        if survival_rate < 0.4:
            return "Moderately Attractive"
        elif 0.4 <= survival_rate < 0.7:
            return "Quite Attractive"
        elif survival_rate >= 0.7:
            return "Highly Attractive"
    elif 4 <= feeders <= 6:
        if survival_rate < 0.5:
            return "Moderately Attractive"
        elif 0.5 <= survival_rate < 0.8:
            return "Quite Attractive"
        elif survival_rate >= 0.8:
            return "Highly Attractive"
    elif 7 <= feeders <= 10:
        if survival_rate < 0.7:
            return "Moderately Attractive"
        elif 0.7 <= survival_rate < 0.9:
            return "Quite Attractive"
        elif survival_rate >= 0.9:
            return "Highly Attractive"
    elif feeders > 10:
        return "Saturated Attractiveness"
    else:
        return "Undefined"

# Main function for user interaction
def main():
    print("Welcome to the Forest Attractiveness Calculator!")
    
    # Loop to allow multiple inputs
    while True:
        try:
            birdfeeders = int(input("Enter the number of bird feeders (or -1 to exit): "))
            
            # Handle exit condition for -1
            if birdfeeders == -1:
                print("Thank you for using the Forest Attractiveness Calculator. Goodbye!")
                break  # Ensure we exit the loop properly
            
            if birdfeeders < 0:
                print("Number of feeders cannot be negative. Please try again.")
                continue
            if birdfeeders > 20:
                print("Allowed number of feeders is between 0 and 20. Please try again.")
                continue

            # User input for the initial survival rate
            initial_survival_rate = float(input("Enter the initial survival rate of birds (between 0.0 and 1.0): "))
            if not (0.0 <= initial_survival_rate <= 1.0):
                print("Invalid input. Survival rate must be between 0.0 and 1.0.")
                continue

            # Classify bird feeders and calculate results
            feeders_segment, survival_rate_range = classify_bird_feeders(birdfeeders)
            final_survival_rate = calculate_survival_rate_with_diminishing_returns(birdfeeders, initial_survival_rate)
            attractiveness = calculate_attractiveness_with_diminishing_returns(birdfeeders, final_survival_rate)

            # Output the results
            print("\nAnalysis Result:")
            print(f"Number of Bird Feeders: {birdfeeders}")
            print(f"Feeders Segment: {feeders_segment}")
            print(f"Initial Survival Rate: {initial_survival_rate:.2f}")
            print(f"Final Survival Rate with Diminished Returns: {final_survival_rate:.2f}")
            print(f"Forest Attractiveness: {attractiveness}")
            print(f"\n{forestattractiveness}")  # Print the constant message
            print("-" * 40)

            # Ask if the user wants to perform another calculation
            new_calc = input("New calculation (y or n)? ").strip().lower()
            if new_calc in ["n", "no"]:
                print("Thank you for using the Forest Attractiveness Calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Execute the main function
if __name__ == "__main__":
    main()




