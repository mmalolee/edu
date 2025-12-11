import itertools

data = ["Normalizacja", "Standaryzacja", "Ewaluacja", "Kredensacja"]


for order in itertools.permutations(data):
    print(f"Pipeline order: {order}")


for order in itertools.permutations(data, 3):
    print(f"Pipeline order: {order}")
