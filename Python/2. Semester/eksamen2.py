test_averages = {'Janelle':98, 'Sam': 87, 'Jennifer':92,'Thomas':74, 'Sally':89, 'Zeb':84}
high_scores = {key:value for (key,value) in test_averages.items() if value > 90}
print(high_scores)