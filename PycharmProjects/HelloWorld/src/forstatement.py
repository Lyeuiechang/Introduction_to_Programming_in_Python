L = [5, -9, -6, 8, 0, 7, 4]
negatives, positives, zeros = 0, 0, 0
for i in L:
    if i > 0:
        positives = positives + 1
    elif i < 0:
        negatives = negatives + 1
    else:
        zeros = zeros + 1
print('>0: %d, <0: %d, ==0: %d' %(positives, negatives, zeros))