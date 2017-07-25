#caprese salad!
ingredients = {}
ingredients['tomatoes'] = 3;
ingredients['ball of mozzarella'] = 1;
ingredients['bunch of basil'] = 1;
ingredients['olive oil'] = 'a splash of';
ingredients['balsamic vinegar'] = 'a splash of';

#print out the ingredients
print("For a caprese salad, you need: ")
for thing in ingredients:
    print(str(ingredients[thing]) + " " + thing)

#steps
steps = []
steps.append("Slice the tomatoes nice and thick.")
steps.append("Slice the mozzarella into the same width slices.")
steps.append("Chop the basil roughly.")
steps.append("Put tomato and mozzarella slices on a plate.")
steps.append("Sprinkle basil, olive oil, and vinegar on top.")
steps.append("YAY now you can eat.")

#print out the steps
print("\nHow to make a caprese salad:")
for number in range(len(steps)-1):
    print(str(number + 1) + ". " + steps[number])
