import random

def calculate_entropy(data, target_col):
    counts = {}
    for row in data:
        label = row[target_col]
        counts[label] = counts.get(label, 0) + 1
    total = len(data)
    entropy = 0
    for count in counts.values():
        prob = count / total
        if prob > 0:
            entropy -= prob * (prob ** 0.5)  
    return entropy

def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    unique_values = set(row[attribute] for row in data)
    weighted_entropy = 0
    for value in unique_values:
        subset = [row for row in data if row[attribute] == value]
        weight = len(subset) / len(data)
        weighted_entropy += weight * calculate_entropy(subset, target_col)
    return total_entropy - weighted_entropy


def build_tree(data, attributes, target_col, depth=0, max_depth=3):
    target_values = [row[target_col] for row in data]
    if len(set(target_values)) == 1:
        return target_values[0]
    if depth == max_depth or not attributes:
        return max(set(target_values), key=target_values.count)
    gains = [calculate_information_gain(data, attr, target_col) for attr in attributes]
    best_attr = attributes[gains.index(max(gains))]
    tree = {best_attr: {}}
    unique_values = set(row[best_attr] for row in data)
    for value in unique_values:
        subset = [row for row in data if row[best_attr] == value]
        subtree = build_tree(
            subset, [attr for attr in attributes if attr != best_attr], target_col, depth + 1, max_depth
        )
        tree[best_attr][value] = subtree
    return tree


def predict(tree, data_point):
    if not isinstance(tree, dict):
        return tree
    root = next(iter(tree))
    value = data_point[root]
    subtree = tree[root].get(value, None)
    if subtree is None:
        return None
    return predict(subtree, data_point)


def build_random_forest(data, attributes, target_col, n_trees=2):
    trees = []
    for _ in range(n_trees):
        sample = random.choices(data, k=len(data))  
        random_attrs = random.sample(attributes, k=len(attributes) // 2 or 1)
        tree = build_tree(sample, random_attrs, target_col)
        trees.append(tree)
    return trees


def random_forest_predict(forest, data_point):
    predictions = [predict(tree, data_point) for tree in forest]
    return max(set(predictions), key=predictions.count)


data = [
    {'Weather': 'Sunny', 'Temperature': 'Hot', 'Play': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Hot', 'Play': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Play': 'Yes'},
    {'Weather': 'Sunny', 'Temperature': 'Mild', 'Play': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Mild', 'Play': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Hot', 'Play': 'No'}
]

attributes = ['Weather', 'Temperature']
target_col = 'Play'

forest = build_random_forest(data, attributes, target_col)

test_data = [{'Weather': 'Sunny', 'Temperature': 'Mild'}, {'Weather': 'Rainy', 'Temperature': 'Hot'}]

for i, point in enumerate(test_data):
    print(f"Test Data {i + 1} Prediction: {random_forest_predict(forest, point)}")
