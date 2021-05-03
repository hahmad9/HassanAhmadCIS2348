"""

Hassan Ahmad
ID: 1865003

"""

#definition of partition function
def partition(arr, lower, higher):
    i = (lower-1)
    pivot = arr[higher]

    #move from left to right
    for j in range(lower, higher):
        if arr[j] <= pivot:
            i = i+1
            #swap the values of i and j
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[higher] = arr[higher], arr[i+1]
    return (i+1)

def Quick_Sort(arr, lower, higher):
    #check if array has only one element
    global num_calls
    num_calls+=1
    if len(arr) == 1:
        return arr

    #traverse till the lower and higher meets
    if lower < higher:
        #calling the partition function for compare
        mid = partition(arr, lower, higher)

            #recursive calling for left and right
        #subarray and store their count
        Quick_Sort(arr, lower, mid-1)
        Quick_Sort(arr, mid+1, higher)


# Driver code to test above
#declaraing an array to store the input
arr = []
while True:
    temp = input()
    if temp == "-1":
        break
    arr.append(temp)
n = len(arr)
num_calls = 0
Quick_Sort(arr, 0, n-1)
#printing the global varialbe num_calls
print(num_calls)
for word in arr:
    print(word)