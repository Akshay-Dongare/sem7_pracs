'''Write a program to solve a fractional Knapsack problem using a greedy method'''
'''Given the weights and profits of N items, in the form of {profit, weight} 
put these items in a knapsack of capacity W to get the maximum total profit in the knapsack. 
In Fractional Knapsack, we can break items for maximizing the total value of the knapsack.'''

def fractional_knapsack(items, capacity):
    '''The basic idea of the greedy approach is to calculate the ratio profit/weight for each item 
    and sort the item on the basis of this ratio. Then take the item with the highest ratio
    and add them as much as we can (can be the whole element or a fraction of it).
    This will always give the maximum profit because, in each step it adds an element such that 
    this is the maximum possible profit for that much weight.'''
    items.sort(key=lambda x: x[1] / x[0], reverse=True) #sorting in descending order based on profit/weight ratio
    total_value = 0
    selected_items = []

    for item in items:
        weight, value = item
        if capacity >= weight:
            total_value += value
            selected_items.append((weight, 1)) #entire item taken so fraction is 1
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += fraction * value
            selected_items.append((weight, fraction))
            break

    return total_value, selected_items

if __name__ == "__main__":
    items = [(10, 60), (20, 100), (30, 120)] #weight,profit
    capacity = 50 #max capacity of knapsack

    max_value, selected_items = fractional_knapsack(items, capacity)

    print("Maximum value:", max_value)
    print("Selected items:")
    for item in selected_items:
        weight, fraction = item
        print(f"Weight: {weight}, Fraction taken: {fraction}")
