# BirdfeedersForest app
#
# to start go to folder birdfeeders and type
#     python.exe .\src\main.py
#
# Copyright (c) by  Shilyn Makin
#



# variable declaration

birdfeeders: int = 0 # number of birdfeeders in the forest
survivalrate: float = 0.0 # the input data given to the program
birdsurvivalrate: float = 0.0 # the calculated survival rate as function of number of feeders
forestattractiveness: str = " The forest is considered more healthy and attractive for visitors due to the increased number of birds"

# function to determine the forest attractiveness
def calculate_attractiveness(feeders):
    if feeders <= 3:
        return "Not very attractive", 
    elif feeders <= 6:
        return "Moderately attractive"
    else:
        return "Highly attractive"
    
# function to deterimne the potential survival rate of birds 
# as function of number of feeders
def calculate_survival_rate(feeders, survivalrate):
    if feeders <= 1:
        return survivalrate
    else:
        return survivalrate * 1.38

# procedure to print results
def print_results(attractiveness, survivalrate):
    print("The forest is considered: ", attractiveness)
    print("Survival rate for birds in areas with feeders: ", survivalrate )
    print('\n')
    

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
            birdsurvivalrate = calculate_survival_rate(birdfeeders, survivalrate)
            print_results(forestattractiveness, birdsurvivalrate)
            if input("new calculation (y or n)? ") == "n":
                break
            else:
                print('\n')
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
