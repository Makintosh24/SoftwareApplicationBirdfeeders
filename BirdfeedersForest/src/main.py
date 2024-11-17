# BirdfeedersForest app
#
# to start go to folder birdfeeders and type
#     python.exe .\src\main.py
#
# Copyright (c) by  Shilyn Makin
#



import math

# Variable declarations
birdfeeders: int = 0  # Number of bird feeders in the forest of 5000 ha

# Calculated final survival rate based on diminishing returns formula
calculated_survival_rate: float = 0.0


# Forest attractiveness description
forestattractiveness: str = "The forest is considered more attractive due to the increased healthier bird population."

# Function to classify bird feeder segments and get survival rate range
def classify_bird_feeders(feeders: int) -> tuple:
    
    # Classify the number of feeders into segments and provide base survival rate range.

    if feeders < 1:
        return 'O', (0.0, 0.0)  # No feeders
    elif 1 <= feeders <= 3:
        return 'A', (0.1, 0.3)  # Segment A: Few feeders
    elif 4 <= feeders <= 6:
        return 'B', (0.3, 0.6)  # Segment B: Moderate number of feeders
    elif feeders >= 7:
        return 'C', (0.6, 0.99)  # Segment C: Many feeders

# Function to calculate survival rate with diminishing returns
def calculate_survival_rate_with_diminishing_returns(feeders: int, min_rate: float) -> float:
    # Calculate the final survival rate with a diminishing returns effect based on the number of feeders.
    return 1


def calculate_survival_rate_with_diminishing_returns(feeders, initial_rate):
    k = 0.38  # Scaling factor for impact of feeders adjusted for 38% higher survival rates
    # Logarithmic function to model diminishing returns
    survival_rate = initial_rate + math.log10(1 + k * feeders)
    # Cap the survival rate between 0.1 and 0.99
    return min(max(survival_rate, 0.1), 0.99)

# Function to determine the forest attractiveness based on diminishing returns
def calculate_attractiveness_with_diminishing_returns(feeders, survival_rate):
    # Adjust attractiveness based on both the number of feeders and the survival rate
    if feeders == 0 or survival_rate < 0.2: 
        return "Not very attractive"
    elif 1 <= feeders <= 3 and survival_rate <= 0.4:
        return "Moderately Attractive"
    elif 4 <= feeders <= 6 and survival_rate <= 0.7:
        return "Quite Attractive"
    elif 7 <= feeders <= 10 and survival_rate <= 0.9:
        return "Highly Attractive"
    else:  # Feeders > 10, where attractiveness plateaus
        return "Saturated Attractiveness"

  
   
# Main function for user interaction
def main():
    print("Welcome to the Bird Conservation Program!")
    
    # Loop to allow multiple inputs
    while True:
        birdfeeders = int(input("Enter the number of bird feeders in the area (or -1 to exit): "))
        
        # Exit condition
        if birdfeeders == -1:
            print("Exiting the program. Thank you!")
            break
        
        # Classify bird feeders and get the survival rate range
        feeders_segment, survival_rate_range = classify_bird_feeders(birdfeeders)
        
        # Calculate survival rate with diminishing returns
        final_survival_rate = calculate_survival_rate_with_diminishing_returns(birdfeeders, survival_rate_range[0])

        # Store the calculated attractiveness
        forestattractiveness = calculate_attractiveness_with_diminishing_returns(birdfeeders, calculated_survival_rate)
    
        # Output the results
        print("\nAnalysis Result:")
        print(f"Number of Bird Feeders: {birdfeeders}")
        print(f"Feeders Segment: {feeders_segment}")
        print(f"Initial Survival Rate (User Input): {initial_survival_rate:.2f}")
        print(f"Calculated Bird Survival Rate with Diminishing Returns: {final_survival_rate:.2f}")
        print(f"Forest Attractiveness: {forestattractiveness}") # Printing the specific attractiveness message
        print("-" * 40)


# main function to control the app
def main():
    print("\nWelcome to the Forest Attractiveness Calculator!")
    # major loop to read in user input
    while True:
        # try to catch eventually ocurring input mistakes
        try:
            birdfeeders = int(input("Enter the number of bird feeders in the forest: "))
            if birdfeeders < 0:
                print("Number of feeders cannot be negative. Please try again.")
                continue
            if birdfeeders>20:
                print ("Allowed number of feeders is 1-20")
                continue
            forestattractiveness = calculate_attractiveness(birdfeeders)
            survivalrate = float(input("Enter the local survival rate of birds: "))
            if survivalrate <= 0:
                print("Survival rate need to be positive. Please try again.")
                continue
            if survivalrate > 100:
                print ("survivalrate cannot exceed 100%" )
                continue

# Normalize survival rate input (percentage to decimal)
            survivalrate /= 100

# User input for the initial survival rate manually
            initial_survival_rate = float(input("Enter the initial survival rate of birds (between 0.0 and 1.0): "))
            if initial_survival_rate < 0 or initial_survival_rate > 1:
                print("Invalid input. Survival rate must be between 0.0 and 1.0.")
                continue

            
            # Calculate the final survival rate using diminishing returns
            feeders_segment, survival_rate_range = classify_bird_feeders(birdfeeders)
            birdsurvivalrate = calculate_survival_rate_with_diminishing_returns(birdfeeders, survival_rate_range[0])

            # Print the results
            print_results(forestattractiveness, birdsurvivalrate)

            # Check if user wants a new calculation
            if input("New calculation (y or n)? ").lower() == "n":
                print("Thank you for using the Forest Attractiveness Calculator. Goodbye!")
                break
            else:
                print('\nStarting a new calculation...\n')
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")

  

# Execute the main function
if __name__ == "__main__":
    main()


