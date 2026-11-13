favorite_foods = ["Tacos", "Ramen", "Pizza", "Injera", "Pierogi"]

for index, food in enumerate(favorite_foods, start=1):

    if index == 1:
        print(f"{index}. {food} <- top pick!")
    else:
        print(f"{index}. {food}")

print("\nList in reverse order:")

for index, food in enumerate(reversed(favorite_foods), start=1):
    if index == 1:
        print(f"{index}. {food} <- top pick!")
    else:
        print(f"{index}. {food}")
