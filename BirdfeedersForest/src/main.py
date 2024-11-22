
# BirdfeedersForest app
#
# to start go to folder birdfeeders and type
#     python.exe .\src\main.py
#
# Copyright (c) by Shilyn Makin

import math

# Variable declarations
birdfeeders: int = 0  # Number of bird feeders in the forest of 5000 ha
calculated_survival_rate: float = 0.0

# Forest attractiveness description
forestattractiveness: str = "The forest is considered more attractive due to the increased healthier bird population."

# Function to classify bird feeder into  segments and get survival rate range
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
def calculate_survival_rate_with_diminishing_returns(feeders: int, initial_rate: float) -> float:
    k = 0.38  # Scaling factor for impact of feeders adjusted for 38% higher survival rates
    # Logarithmic function to model diminishing returns
    survival_rate = initial_rate + math.log10(1 + k * feeders)
    # Cap the survival rate between 0.1 and 0.99
    return min(max(survival_rate, 0.1), 0.99)

 # Check if feeders are more than 10 (plateau case first)
    if feeders > 10:  
        return "Saturated Attractiveness"
    # Now, evaluate attractiveness based on both feeders and survival rate
# Function to determine the forest attractiveness based on diminishing returns
def calculate_attractiveness_with_diminishing_returns(feeders: int, survival_rate: float) -> str:
    # Adjust attractiveness based on both the number of feeders and the survival rate
    if feeders == 0 or survival_rate < 0.2: 
        return "Not very attractive"
    elif 1 <= feeders <= 3 and survival_rate <= 0.4:
        return "Moderately Attractive"
    elif 4 <= feeders <= 6 and survival_rate <= 0.7:
        return "Quite Attractive"
    elif 7 <= feeders <= 10 and survival_rate <= 0.99:
        return "Highly Attractive"
    elif feeders > 10:  # Feeders > 10, where attractiveness plateaus
        return "Saturated Attractiveness"



# Main function for user interaction
def main():
    print("Welcome to the Forest Attractiveness Calculator!")

   # Loop to allow multiple inputs
    while True:
        try:
            # User input for the number of bird feeders
                        birdfeeders = int(input("Enter the number of bird feeders (or -1 to exit): "))
            if birdfeeders == -1:
                break  # Exit the loop if user inputs -1
    
                print("Exiting the program. Thank you!")
                break 
           if birdfeeders <0
                        print("Number of feeders cannot be negative. Please try again.")
                continue
            if birdfeeders > 20:
                print("Allowed number of feeders is between 0 and 20. Please try again.")
                continue


    
    

            # User input for the initial survival rate manually
            initial_survival_rate = float(input("Enter the initial survival rate of birds (between 0.0 and 1.0): "))
            if initial_survival_rate < 0 or initial_survival_rate > 1:
                if not (0.0 <= initial_survival_rate <= 1.0):                
                print("Invalid input. Survival rate must be between 0.0 and 1.0.")
                continue



            # Classify bird feeders and get the survival rate range
            feeders_segment, survival_rate_range = classify_bird_feeders(birdfeeders)

            # Calculate the final survival rate using diminishing returns
            final_survival_rate = calculate_survival_rate_with_diminishing_returns(birdfeeders, survival_rate_range[0])

            # Calculate forest attractiveness
            forestattractiveness = calculate_attractiveness_with_diminishing_returns(birdfeeders, final_survival_rate)


            # Output the results
            print("\nAnalysis Result:")
            print(f"Number of Bird Feeders: {birdfeeders}")
            print(f"Feeders Segment: {feeders_segment}")
            print(f"Initial Survival Rate: {initial_survival_rate:.2f}")
            print(f"Final Survival Rate with Diminished Returns: {final_survival_rate:.2f}")
            print(f"Forest Attractiveness: {attractiveness}")
            print("-" * 40)

            # Ask whether the  user wants to perform another calculation
            if input("New calculation (y or n)? ").strip().lower() in ["n", "no"]:


            # Check if the user wants a new calculation
            if input("New calculation (y or n)? ").lower() == "n":
            
                break
            else:
                print('\nStarting a new calculation...\n')

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Exit message
    print("Thank you for using the Forest Attractiveness Calculator. Goodbye!"


# Execute the main function
if __name__ == "__main__":
    main()
