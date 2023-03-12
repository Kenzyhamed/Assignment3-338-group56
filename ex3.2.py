import json
import timeit
from urllib.request import urlopen
import matplotlib.pyplot as plt
def binary_search( arr, x, pick_position):
    low = 0
    high = len(arr) - 1
    position_picker_flag = False
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
        return -1
        if position_picker_flag == True:
            pos = (low+hign) //2 
        if position_picker_flag == False:
            pos = pick_position
            position_picker_flag = True
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low=pos +1
        else:
            high=pos-1
    return -1
def main():
    with urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json') as inUrl:
        arr_search = json.load(inUrl)
    with urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json') as inUrl:
        arr_tasks = json.load(inUrl)

    j=0
    timef =[]
    midpoints = arr_tasks
    task_list= range(len(arr_tasks) )

    while j != len(arr_tasks) :
        timef.append(timeit.timeit(f'binary_search({arr_search},{arr_tasks[j]},{arr_tasks[j]})',setup='from __main__ import binary_search',number=100))
        j+=1
    #this timing graph slows down the program significantly
    '''plt.subplot(1, 2, 1)
    pit.scatter(task_list, timef, label='Time to find task 100 times')
    plt.title('Time vs task number')
    pit.xlabel ('Task Number')
    pit.ylabel ('Time (s) ')
    plt.legend()'''
    #plt. subplot (1, 2,2) 
    plt.scatter(task_list, midpoints, label='Chosen Midpoints') 
    plt.legend()
    plt.title( 'Chosen Midpoint vs task number')
    plt.xlabel('Task Number')
    plt.ylabel('Chosen Midpoint' )
    
if __name__ == "__main__" :
        main()




