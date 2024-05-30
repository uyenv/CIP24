#Explanations for Lecture 11: Memory Model

def main():
    arr = [9, 8, 7, 6]
    plus(arr)
    print(arr)

    """
def plus(array):
    for i in range (0, len(array)): #array[i] element taking out from array was
        array[i] += 1               #the same element coming from an array (a reference)
    #[10, 9, 8, 7]                  #since the array type was mutable
    """

def plus(array):
    for element in array: #element taking out from array was
        element += 1       #an immutable int (a copy of each element from the array)
    #[9, 8, 7, 6]

if __name__ == "__main__":
    main()
