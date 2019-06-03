def print_array(array):
    for i in range(len(array)):
        print("%2s" %("  ".join(array[i])))

    return


if __name__ == "__main__":
    array = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 0, 9, 8],
        [7, 6, 5, 4, 3, 2]]
    
    print_array(array)