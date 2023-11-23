def bubble_sort(data, start=0, end=None):
    if end is None:
        end = len(data)
    for i in range(start, end):
        for j in range(0, end - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                yield data[:], (j, j + 1), i  # Include the current outer loop index
            else:
                yield data[:], (j, j + 1), i
