import random

# Get number of friends
num_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    # Create the dictionary of friends
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input()
        friends[name] = 0

    # Get the total bill value
    total_bill = float(input("Enter the total bill value:\n"))

    # Ask user if they want to use the "Who is lucky?" feature
    use_lucky = input("Do you want to use the 'Who is lucky?' feature? (Yes/No):\n")

    if use_lucky == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")

        split_value = round(total_bill / (num_friends - 1), 2)

        for person in friends:
            friends[person] = 0 if person == lucky else split_value
    else:
        print("No one is going to be lucky")
        split_value = round(total_bill / num_friends, 2)
        for person in friends:
            friends[person] = split_value

    print(friends)
