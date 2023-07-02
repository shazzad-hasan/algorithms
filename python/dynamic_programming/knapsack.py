"""
Suppose you are about to sit to a meal. You know how much you value
different foods e.g., you like pizza more than burger, but you have
a calorie budget. In this case, choosing what to eat is a 
knapsack problem. 

In the follwoing, we use a greedy approach to decide what to order subject
to the constraint that we don't want to consume more than a specific 
amout of calories.

Complexity: n log n
""" 
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

def buildMenu(names, values, calories):
    menu = [Food(names[i], values[i], calories[i]) for i in range(len(values))]
    return menu

def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)   # O(nlogn)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):                                # O(n)
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, value = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', value)
    for item in taken:
        print('  ', item)

def main(): 
    names = ['wine', 'beer', 'pizza', 'burger', 'fries',
            'cola', 'apple', 'donut', 'cake']
    values = [89,90,95,100,90,79,50,10]
    calories = [123,154,258,354,365,150,95,195]
    foods = buildMenu(names, values, calories)

    constraint = 1000
    print("Greedy by value")
    testGreedy(foods, constraint, Food.getValue)
    print("Greedy by cost")
    testGreedy(foods, constraint, lambda x: 1/Food.getCost(x))
    print("Greedy by density")
    testGreedy(foods, constraint, Food.density)

if __name__=="__main__":
    main()





