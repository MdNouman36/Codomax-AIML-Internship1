def calculate_accuracy(predictions, actuals):
    correct = 0
    for i in range(len(predictions)):
        if predictions[i] == actuals[i]:
            correct += 1
    accuracy = (correct / len(actuals)) * 100
    return accuracy


def classify_temperature(temp_list):
    results = []
    for temp in temp_list:
        if temp >= 30:
            results.append("High")
        elif temp >= 20:
            results.append("Normal")
        else:
            results.append("Low")
    return results


def summarize_dataset(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    highest = max(numbers)
    lowest = min(numbers)
    return {
        "count": count,
        "average": round(average, 2),
        "max": highest,
        "min": lowest
    }


if __name__ == "__main__":
    intern_name = "Mohammed Nouman M N"
    module_number = 1
    print(f"Intern: {intern_name} | Module: {module_number}")

    actual_labels = [1, 0, 1, 1, 0, 1, 0, 0]
    predicted_labels = [1, 0, 1, 0, 0, 1, 1, 0]
    model_accuracy = calculate_accuracy(predicted_labels, actual_labels)
    print(f"Model Accuracy: {model_accuracy}%")

    sensor_readings = [18.5, 24.0, 32.1, 29.8, 15.2, 35.0]
    classifications = classify_temperature(sensor_readings)
    print("Temperature Classifications:", classifications)

    stats = summarize_dataset(sensor_readings)
    print("Dataset Summary:", stats)
