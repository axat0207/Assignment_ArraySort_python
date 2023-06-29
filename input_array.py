def get_input_array():
    # Take input for array size
    n = int(input("Enter the size of the array: "))

    # Initialize an empty array
    arr = []

    # Take input for each element of the array
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)

    return arr


def display_array(arr):
    # Print the array
    print("Array elements:")
    for element in arr: 
        print(element)


# Main program
if __name__ == "__main__":
    # Get input array from the user
    input_arr = get_input_array()

    # Display the input array
    display_array(input_arr)
