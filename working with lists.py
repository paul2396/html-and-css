my_list = ["s", "a", "x", "s", "n", "z", "a", "l", "h", "l", "k", "g", "v","f"]
list1 = list(range(10))
list2 = list(range(1, 11))
print(list1)
print(my_list)
my_list.sort()
print(my_list)
my_list.append("q")
print(my_list)
my_list.insert(0,"o")
print(my_list)
my_list.reverse()
print(my_list)
my_list.remove("v")
print(my_list)
print(my_list[1:4])
print(my_list[:4])
list(range(10))
print("here are the first three letters on my list")
for my_list in my_list[:3]:
    print(my_list.title())

my_foods = ["pizza", "falafel", "carrot cake"]
friend_food = my_foods[:]  # Use my_foods instead of my_food
print("my favorite foods are:")
print(my_foods)
print("\nmy friend's favorite are:")
print(friend_food)
my_foods.append("cannoli")
friend_food.append("ice cream")
print("my favorite foods are")
print(my_foods)
print("my friends favorite foods are")
print(friend_food)
cars=["audi","bmw","subaru","toyota"]
for car in cars:
    if car=="bmw":
        print(car.upper())
    else:
        print(car.title())
        car="bmw"
        car=="bmw"

import lancaster_module



def main():
    root = tk.Tk()
    root.title("Tkinter Test")
    root.mainloop()


 




