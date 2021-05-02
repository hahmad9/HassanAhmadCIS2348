"""

Hassan Ahmad
ID: 1865003

"""

# function to read age from inputs
def get_age():
    age = int(input())
    if age < 18 or age > 75:  
        raise ValueError("Invalid age.") 
    return age  


# function to calculate heart rate
def fat_burning_heart_rate(age):  

    heart_rate = 220 - age
    heart_rate *= 0.7
    return heart_rate

if __name__ == "__main__":

    # try block of statements
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a", age, "year-old:", rate, "bpm")

    # If exception occurs, handle them with printing message on console
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.')
        print()
