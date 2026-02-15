# Function to get valid input for a test score
def get_valid_test_score () :
    while True:
        try:
            score = float(input ("Enter a test score: ") )
            if 0 <= score <= 100:
                return score
            else:
                print ("Please enter a valid test score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Input three test scores for a single student
test_scores = []

for i in range (3) :
    test_scores.append(get_valid_test_score ())

# Sort the test scores in descending order
test_scores.sort (reverse=True)

# Calculate the average of the best two test scores
best_two_averages = sum(test_scores [:2]) / 2

# Output the result
print (f"The average of the best two test scores is: {best_two_averages: .2f}")