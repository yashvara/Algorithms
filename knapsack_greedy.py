def knapsack_greedy(values, weights, capacity):
    n = len(values)
    value_per_weight = [(values[i] / weights[i], values[i], weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)

    total_value = 0
    knapsack = [0] * n

    for i in range(n):
        value, weight, index = value_per_weight[i]
        if weight <= capacity:
            knapsack[index] = 1
            total_value += value
            capacity -= weight
        else:
            knapsack[index] = capacity / weight
            total_value += capacity / weight * value
            break

    return total_value, knapsack

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, selected_items = knapsack_greedy(values, weights, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
