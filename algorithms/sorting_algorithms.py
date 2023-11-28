def bubble_sort(data, start=0, end=None, comparisons=0, swaps=0):
    if end is None:
        end = len(data)

    for i in range(start, end):
        for j in range(0, end - i - 1):
            comparisons += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
            yield data[:], (j, j + 1), i, comparisons, swaps
