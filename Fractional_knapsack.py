def fractional_knapsack(pr, wt, W, n):
  # Sort the items in decreasing order of value per weight.
  items = sorted(zip(pr, wt), key=lambda x: x[0] / x[1], reverse=True)

  # Initialize the total value and the total weight.
  total_value = 0
  total_weight = 0

  # Add items to the knapsack in order of value per weight, until the knapsack is
  # full or there are no more items to add.
  for item in items:
    if total_weight + item[1] <= W:
      total_value += item[0]
      total_weight += item[1]
    else:
      # Add a fraction of the last item to the knapsack until the knapsack is
      # full.
      fraction = (W - total_weight) / item[1]
      total_value += fraction * item[0]
      total_weight += fraction * item[1]
      break

  return total_value

pr = [7,6,67,56,98,1]
wt = [2,3,4,2,9,5]
W = 10
n = len(pr)
print(fractional_knapsack(pr, wt, W, n))

