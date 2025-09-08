# in arrary any duplicate element is present then return True otherwise false
from utils import TestResult


def find_duplicate1(arr: list) -> bool:
    # if the lenth of array is equal to the length od set created from array then return false otherwise true
    return len(arr) != len(set(arr))


def find_duplicate2(arr: list) -> bool:
    # create set which contain the unique element ,compare each element from arr  to  unique_elements if present the return true else add element in unique_elements.
    # return the final result as false after loop complete.
    unique_elements = set()
    for i in arr:
        if i in unique_elements:
            return True
        else:
            unique_elements.add(i)
    return False


def find_duplicate3(arr: list) -> bool:
    # using brute force
    # compare each element from arr and check element is present or not
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            # print('i and j',i,j)
            if arr[i] == arr[j]:
                return True
    return False


def find_duplicate4(arr: list):
    # sort the arr, check adjecnt element is equal or not
    arr1 = arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return True
    return False


if __name__ == "__main__":
    result_check_data = [
        {'params': {'arr': [1, 2, 3, 3]}, 'result': True},
        {'params': {'arr': [1, 2, 3, 4]}, 'result': False}
    ]

    testobj = TestResult(result_check_data)
    testobj.test_all_scenarios(find_duplicate1)
    testobj.test_all_scenarios(find_duplicate2)
    testobj.test_all_scenarios(find_duplicate3)
    testobj.test_all_scenarios(find_duplicate4)
