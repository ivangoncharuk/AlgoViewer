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


def quick_sort(data, low=0, high=None, comparisons=0, swaps=0):
    if high is None:
        high = len(data) - 1

    if low < high:
        pivot_index, comparisons, swaps, partition_steps = partition(
            data, low, high, comparisons, swaps
        )

        for step in partition_steps:
            yield step

        for state in quick_sort(data, low, pivot_index - 1, comparisons, swaps):
            yield state

        for state in quick_sort(data, pivot_index + 1, high, comparisons, swaps):
            yield state


def partition(data, low, high, comparisons, swaps):
    pivot = data[high]
    i = low - 1
    steps = []

    for j in range(low, high):
        comparisons += 1
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            swaps += 1
            steps.append((data[:], (i, j), high, comparisons, swaps))

    data[i + 1], data[high] = data[high], data[i + 1]
    swaps += 1
    pivot_index = i + 1

    return pivot_index, comparisons, swaps, steps
