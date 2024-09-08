# 4) Write a Program that takes the array of five element and the elements of that array are accessed using pointer.

class PointerArray:
    def __init__(self, size):
        self.size = size
        self.array = [0] * size

    def set_value(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            print("Index out of bounds")

    def get_value(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            print("Index out of bounds")
            return None

    def display_array(self):
        print("Array elements are:", self.array)

def main():
    size = 5
    pointer_array = PointerArray(size)

    print(f"Enter {size} elements:")
    for i in range(size):
        value = float(input(f"Enter element {i + 1}: "))
        pointer_array.set_value(i, value)

    pointer_array.display_array()

    print("Accessing elements using simulated pointers:")
    for i in range(size):
        value = pointer_array.get_value(i)
        print(f"Element at index {i} is {value}")

if __name__ == "__main__":
    main()
