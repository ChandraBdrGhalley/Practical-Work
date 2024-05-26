def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(sorted_arr, target, replacement):
    for i in range(len(sorted_arr)):
        if sorted_arr[i] == target:
            sorted_arr[i] = replacement
    return sorted_arr

def main():
    user_input = input("Enter integers separated by spaces: ")
    input_array = list(map(int, user_input.split()))

    sorted_array = quick_sort(input_array)
    print("Sorted Array:", sorted_array)

    target_element = int(input("Enter the target element to serach for: "))

    if target_element in sorted_array:
        replacement_element = int(input("Enter the replacement element: "))
        sorted_array = replace_elements(sorted_array, target_element, replacement_element)
        print("Modified Array after replacing elements:", sorted_array)
    else:
        print("Target element not found in the array.")

if __name__ == "__main__":
    main()