# Muhammad Ryhan
# F5121008
import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    return arr, end_time - start_time

def print_iterations(arr):
    print("5 iterasi pertama:")
    for i in range(min(5, len(arr))):
        print(arr[i], end=" ")
    print("\n5 iterasi terakhir:")
    for i in range(max(0, len(arr) - 5), len(arr)):
        print(arr[i], end=" ")
    print()

def print_before_after(arr):
    print("Sebelum pengurutan:")
    print(arr)
    sorted_arr, _ = bubble_sort(arr.copy())  # Pengurutan menggunakan bubble sort
    print("Setelah pengurutan:")
    print(sorted_arr)

def main():
    arr = [
        12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55,
        33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23,
        63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1,
        32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81
    ]

    while True:
        print("Silahkan Pilih Algoritma Pengurutan:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Keluar")
        choice = int(input("Masukkan pilihan Anda (1, 2, atau 3): "))

        if choice == 1:
            sorted_arr, runtime = bubble_sort(arr)
            print("Bubble Sort:")
            print_iterations(sorted_arr)
            print("Waktu Komputasi:", runtime, "detik")
            print_before_after(arr)
        elif choice == 2:
            sorted_arr, runtime = insertion_sort(arr)
            print("Insertion Sort:")
            print_iterations(sorted_arr)
            print("Waktu Komputasi:", runtime, "detik")
            print_before_after(arr)
        elif choice == 3:
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == '__main__':
    main()