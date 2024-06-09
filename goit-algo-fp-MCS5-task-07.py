import random
import pandas as pd


def simulate_dice_rolls(num_rolls):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1

    probabilities = {key: value / num_rolls for key, value in results.items()}
    return probabilities

analytical_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

num_rolls = 1000000

simulated_probabilities = simulate_dice_rolls(num_rolls)

results_table = pd.DataFrame({
    "Сумма": list(range(2, 13)),  # Суммы от 2 до 12
    "Монте-Карло": [simulated_probabilities[key] for key in range(2, 13)],
    "Аналитическая": [analytical_probabilities[key] for key in range(2, 13)]
})

print(results_table)
