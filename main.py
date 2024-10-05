import random
import timeit
import pandas as pd
from manual_merge_sort import merge_sort
from manual_insertion_sort import insertion_sort

def generate_data(n):
    random_data = random.sample(range(n * 2), n)  
    return random_data

def main():
    arr_sizes = [100, 1000, 10000]
    algorithms = ["Merge Sort", "Insertion Sort", "Timsort"]
    results = []

    for n in arr_sizes:
        random_data = generate_data(n)
        copied_data = random_data.copy()
        
        for alg in algorithms:
            if alg == "Merge Sort":
                time = timeit.timeit(lambda: merge_sort(copied_data), number=1)
            elif alg == "Insertion Sort":
                time = timeit.timeit(lambda: insertion_sort(copied_data), number=1)
            elif alg == "Timsort":
                time = timeit.timeit(lambda: sorted(copied_data), number=1)
            results.append([alg, n, format(time, ".6f")])

    df = pd.DataFrame(results, columns=["Algorithm", "Size", "Time (seconds)"])
    df_pivot = df.pivot(index="Algorithm", columns="Size", values="Time (seconds)")
    print(df_pivot)
    print("\nДля малих масивів Timsort працює у десятки разів швидше,")
    print("а зі збільшенням кількості елементів виконання вже йде у сотні разів швидше")

main()