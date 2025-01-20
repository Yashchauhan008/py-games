import matplotlib.pyplot as plt
import random
import time

# Sorting Algorithms
def heapify(data, n, i, draw_bars, delay):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[largest] < data[left]:
        largest = left

    if right < n and data[largest] < data[right]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        draw_bars(data)
        plt.pause(delay)
        heapify(data, n, largest, draw_bars, delay)

def heap_sort(data, draw_bars, delay):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, draw_bars, delay)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        draw_bars(data)
        plt.pause(delay)
        heapify(data, i, 0, draw_bars, delay)

def bucket_sort(data, draw_bars, delay):
    max_value = max(data)
    size = max_value // len(data) + 1
    buckets = [[] for _ in range(len(data))]

    for num in data:
        index = num // size
        buckets[index].append(num)

    for i in range(len(buckets)):
        buckets[i].sort()
        draw_bars(flatten(buckets))
        plt.pause(delay)

    result = []
    for bucket in buckets:
        result.extend(bucket)
        draw_bars(result + flatten(buckets[len(result):]))
        plt.pause(delay)
    for i in range(len(data)):
        data[i] = result[i]

def flatten(buckets):
    return [num for bucket in buckets for num in bucket]

# Visualization Function
def visualize_sorting():
    # Generate random data
    data1 = [random.randint(1, 200) for _ in range(200)]
    data2 = data1.copy()

    # Set up the figure and axes
    fig, axes = plt.subplots(1, 2, figsize=(12, 6), dpi=100)
    bars1 = axes[0].bar(range(len(data1)), data1, color='green')
    bars2 = axes[1].bar(range(len(data2)), data2, color='green')

    # Hide axes and borders
    for ax in axes:
        ax.axis("off")

    # Function to update the bars
    def draw_bars1(data):
        for bar, height in zip(bars1, data):
            bar.set_height(height)

    def draw_bars2(data):
        for bar, height in zip(bars2, data):
            bar.set_height(height)

    # Start sorting and measure time
    start_bucket = time.time()
    bucket_sort(data1, draw_bars1, delay=0.001)
    bucket_time = time.time() - start_bucket

    start_heap = time.time()
    heap_sort(data2, draw_bars2, delay=0.001)
    heap_time = time.time() - start_heap

    # Add time taken and algorithm names below the charts
    axes[0].text(0.5, -0.1, f"Bucket Sort\nTime: {bucket_time:.2f}s", ha='center', va='center',
                 transform=axes[0].transAxes, fontsize=12, color='white')
    axes[1].text(0.5, -0.1, f"Heap Sort\nTime: {heap_time:.2f}s", ha='center', va='center',
                 transform=axes[1].transAxes, fontsize=12, color='white')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_sorting()
