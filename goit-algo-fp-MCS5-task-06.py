items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    items_ratio = [(item, data["calories"] / data["cost"]) for item, data in items.items()]
    items_ratio.sort(key=lambda x: x[1], reverse=True)  # Сортування за спаданням співвідношення

    selected_items = []
    total_calories = 0
    for item, _ in items_ratio:
        if items[item]["cost"] <= budget:
            selected_items.append(item)
            total_calories += items[item]["calories"]
            budget -= items[item]["cost"]

    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if items[list(items.keys())[i - 1]]["cost"] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - items[list(items.keys())[i - 1]]["cost"]] + items[list(items.keys())[i - 1]]["calories"],
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    total_calories = dp[n][budget]
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(list(items.keys())[i - 1])
            w -= items[list(items.keys())[i - 1]]["cost"]

    return selected_items, total_calories

budget = int(input("Введіть бюджет: "))

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("\nЖадібний алгоритм:")
print("Обрані страви:", greedy_result[0])
print("Загальна калорійність:", greedy_result[1])

print("\nДинамічне програмування:")
print("Обрані страви:", dp_result[0])
print("Загальна калорійність:", dp_result[1])
