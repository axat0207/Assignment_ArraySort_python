def sort_array(arr):
    # Sort the array in ascending order
    arr.sort()

    return arr


# Main program
if __name__ == "__main__":
    from input_array import get_input_array, display_array

    # Get input array from the user
    input_arr = get_input_array()

    # Display the array
    print("Before Sorting:")
    display_array(input_arr)

    # Sort the array
    sorted_arr = sort_array(input_arr)

    # Display the sorted array
    print("After Sorting:")
    display_array(sorted_arr)
