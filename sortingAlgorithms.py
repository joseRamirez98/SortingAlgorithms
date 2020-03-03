import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

MAX_ROWS = 100
MAX_COLMS = 100

def main():
    arr = np.random.randint(1,100,size=(MAX_ROWS, MAX_COLMS))
    
    df = pd.DataFrame()
    fig=plt.figure()
    ax=fig.add_subplot(111)

    temp_arr = copyArr(arr)
    plotWriteRunTimes(df,ax, 'blue', "bubbleSort", bubbleSort, temp_arr, MAX_ROWS-1)

    temp_arr = copyArr(arr)
    plotWriteRunTimes(df, ax, 'red', "selectionSort", selectionSort, temp_arr, MAX_ROWS-1)

    temp_arr = copyArr(arr)
    plotWriteRunTimes(df, ax, 'green', "shellSort", shellSort, temp_arr, MAX_ROWS)

    temp_arr = copyArr(arr)
    plotWriteRunTimes(df, ax, 'orange', "insertionSort", insertionSort, temp_arr)

    plt.legend(loc='upper right')
    plt.title('Runtimes Over 100 Iterations For Each Sorting Algorithm')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Runtime in Seconds')
    plt.savefig("runtimes.jpg", dpi=500)

    df.to_csv("runtimes.csv")

def plotWriteRunTimes(df, ax, color, func_name, func, *args):
    wrapped = wrapper(func,*args)
    runtime_list = timeit.repeat(wrapped, number=1, repeat=100)
    x=np.array(range(len(runtime_list)))
    ax.plot(x, runtime_list, c=color, label=func_name)
    addDataToDataFrame(df, runtime_list, func_name)

def addDataToDataFrame(df, runtime_list, func_name):
    df[func_name] = runtime_list

def bubbleSort(arr, limit):
    temp = 0
    columnToSort = 0
    while limit > 0:
        for index in range(0, limit):
            if arr[index][columnToSort] > arr[index + 1][columnToSort]:
                for j in range(0,MAX_COLMS):
                    temp = arr[index][j]
                    arr[index][j] = arr[index+1][j]
                    arr[index+1][j] = temp
        limit -= 1

def selectionSort(arr, limit):
    temp = 0
    columnToSort = 1

    while limit > 0:
        indexOfLargest = 0
        for index in range(1, limit+1):
            if arr[index][columnToSort] < arr[indexOfLargest][columnToSort]:
                indexOfLargest = index
        if limit != indexOfLargest:
            for j in range(0, MAX_COLMS):
                temp = arr[limit][j]
                arr[limit][j] = arr[indexOfLargest][j]
                arr[indexOfLargest][j] = temp
        limit -= 1

def shellSort(arr, n):
    temp = 0
    columnToSort = 2
    gap = n//2

    while gap >= 1:
        i = gap
        for i in range(gap,n):
            j = i
            while  j >= gap and arr[j-gap][columnToSort] > arr[j][columnToSort]:
                for column in range(0, MAX_COLMS):
                    temp = arr[j-gap][column]
                    arr[j-gap][column] = arr[j][column]
                    arr[j][column] = temp
                j -= gap
        gap = gap // 2

def insertionSort(arr):
    temp = 0
    rowToSort = MAX_ROWS - 1

    for i in range(1, MAX_COLMS):
        j = i
        while j > 0 and arr[rowToSort][j - 1] > arr[rowToSort][j]:
                for row in range(0,MAX_ROWS):
                    temp = arr[row][j];
                    arr[row][j] = arr[row][j-1];
                    arr[row][j-1] = temp;
                j-=1
                
def copyArr(arr):
    temp_arr = [[0 for x in range(MAX_COLMS)] for y in range(MAX_ROWS)]

    for i in range(0, MAX_ROWS):
        for j in range(0, MAX_COLMS):
            temp_arr[i][j] = arr[i][j]
    return temp_arr

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

main()
