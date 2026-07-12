fruit=['Apple','Orange','Grapes','Mango','Pear']
for i in fruit: 
    print(i)  

new_fruit = input("Enter a new fruit: ")
fruit.append(new_fruit)
print("After adding a fruit: ")
print(fruit)

remove_fruit = input("Enter the fruit to remove: ")
fruit.remove(remove_fruit)
print("\nAfter removing a fruit:")
print(fruit)

# Print first and last element
print("\nFirst Element:", fruit[0])
print("Last Element:", fruit[-1])