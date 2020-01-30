print("Welcome to the MPH to MPS conversion app")

mph = float(input("\nWhat is your speed in miles per hour: "))

mps = mph*0.4474
mps = round(mps, 2)

print(f"\nYour speed in meters per second is {mps}")