# Hassan Ahmad
# ID: 1865003

def exact_change(user_total):
    dollar = user_total // 100
    user_total = user_total % 100
    quarter = user_total // 25
    user_total = user_total % 25
    dime = user_total // 10
    user_total = user_total % 10
    nickel = user_total // 5
    user_total = user_total % 5
    penny = user_total

    if dollar == 1:
        print("1 dollar")
    if dollar > 1:
        print(dollar, "dollars")
    if quarter == 1:
        print("1 quarter")
    if quarter > 1:
        print(quarter, "quarters")
    if dime == 1:
        print("1 dime")
    if dime > 1:
        print(dime, "dimes")
    if nickel == 1:
        print("1 nickel")
    if nickel > 1:
        print(nickel, "nickels")
    if penny == 1:
        print("1 penny")
    if penny > 1:
        print(penny, "pennies")
    if dollar < 1 and quarter < 1 and dime < 1 and nickel < 1 and penny < 1:
        print("no change")


num = int(input())
exact_change(num)
