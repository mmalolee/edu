import itertools

seq1 = [1, 2]
seq2 = [1, 2, 3, 4]
padded = list(itertools.zip_longest(seq1, seq2, fillvalue=2222))
print(padded)
