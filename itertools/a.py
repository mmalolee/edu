import itertools

data = ["Normalizacja", "Standaryzacja", "Ewaluacja", "Kredensacja"]


for order in itertools.permutations(data): # zmienia kolejność w całej liście
    print(f"Pipeline order: {order}")

# Pipeline order: ('Normalizacja', 'Standaryzacja', 'Ewaluacja', 'Kredensacja')
# Pipeline order: ('Normalizacja', 'Standaryzacja', 'Kredensacja', 'Ewaluacja')
# Pipeline order: ('Normalizacja', 'Ewaluacja', 'Standaryzacja', 'Kredensacja')
# Pipeline order: ('Normalizacja', 'Ewaluacja', 'Kredensacja', 'Standaryzacja')


for order in itertools.permutations(data, 3): # zmienia
    print(f"Pipeline order: {order}")

# Pipeline order: ('Normalizacja', 'Standaryzacja', 'Ewaluacja')
# Pipeline order: ('Normalizacja', 'Standaryzacja', 'Kredensacja')
# Pipeline order: ('Normalizacja', 'Ewaluacja', 'Standaryzacja')
# Pipeline order: ('Normalizacja', 'Ewaluacja', 'Kredensacja')
# Pipeline order: ('Normalizacja', 'Kredensacja', 'Standaryzacja')
# Pipeline order: ('Normalizacja', 'Kredensacja', 'Ewaluacja')
# Pipeline order: ('Standaryzacja', 'Normalizacja', 'Ewaluacja')
# Pipeline order: ('Standaryzacja', 'Normalizacja', 'Kredensacja') ...

