def knapsack_greedy(weights, values, capacity):
    ratios = [v / w for v, w in zip(values, weights)]
    sorted_items = sorted(zip(ratios, weights, values), reverse=True)
    total_value = 0
    selected_items = []
    
    for ratio, weight, value in sorted_items:
        if capacity >= weight:
            selected_items.append((weight, value))
            total_value += value
            capacity -= weight
    
    return total_value, selected_items

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value, selected_items = knapsack_greedy(weights, values, capacity)

print("Maximum value:", max_value)
print("Selected items:", selected_items)

