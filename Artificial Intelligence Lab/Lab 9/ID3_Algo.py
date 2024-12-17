def calculate_entropy(data, target_col):
    values = [row[target_col] for row in data]
    unique_values = set(values)
    total = len(values)
    counts = {val: values.count(val) for val in unique_values}
    entropy = 0
    for count in counts.values():
        prob = count / total
        entropy -= prob * (0 if prob == 0 else (prob ** 0.5))
    return entropy

def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    values = [row[attribute] for row in data]
    unique_values = set(values)
    total = len(values)
    weighted_entropy = 0
    for value in unique_values:
        subset = [row for row in data if row[attribute] == value]
        weight = len(subset) / total
        weighted_entropy += weight * calculate_entropy(subset, target_col)
    gain = total_entropy - weighted_entropy
    return gain

def build_tree(data, attributes, target_col):
    target_values = [row[target_col] for row in data]
    if len(set(target_values)) == 1:
        return target_values[0]
    if not attributes:
        return max(set(target_values), key=target_values.count)
    gains = [calculate_information_gain(data, attr, target_col) for attr in attributes]
    best_attribute = attributes[gains.index(max(gains))]
    tree = {best_attribute: {}}
    unique_values = set(row[best_attribute] for row in data)
    for value in unique_values:
        subset = [row for row in data if row[best_attribute] == value]
        if not subset:
            majority_value = max(set(target_values), key=target_values.count)
            tree[best_attribute][value] = majority_value
        else:
            subtree = build_tree(
                subset, [attr for attr in attributes if attr != best_attribute], target_col
            )
            tree[best_attribute][value] = subtree
    return tree

def predict(tree, data_point):
    if not isinstance(tree, dict):
        return tree
    attribute = next(iter(tree))
    value = data_point.get(attribute, None)
    if value not in tree[attribute]:
        return None
    return predict(tree[attribute][value], data_point)

data = [
    {'Weather': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'Play': 'No'},
    {'Weather': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Strong', 'Play': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'Play': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong', 'Play': 'Yes'},
    {'Weather': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak', 'Play': 'No'},
    {'Weather': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Weather': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Wind': 'Strong', 'Play': 'Yes'},
    {'Weather': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'Play': 'Yes'},
    {'Weather': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'Normal', 'Wind': 'Weak', 'Play': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Strong', 'Play': 'No'}
]

target_col = 'Play'
attributes = ['Weather', 'Temperature', 'Humidity', 'Wind']

decision_tree = build_tree(data, attributes, target_col)

test_data = [
    {'Weather': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Wind': 'Strong'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Humidity': 'High', 'Wind': 'Weak'},
]

predictions = [predict(decision_tree, row) for row in test_data]
for i, prediction in enumerate(predictions):
    print(f"Test Data {i + 1} Prediction: {prediction}")
