# in arrary any duplicate element is present then return True otherwise false
from utils import TestResult


def find_duplicate1(arr):
    # if the lenth of array is equal to the length od set created from array then return false otherwise true
    return len(arr) != len(set(arr))

def find_duplicate2(arr):
    unique_elements=set()
    for i in arr:
        if i in unique_elements:
            return True
        else:
            unique_elements.add(i)
    return False

if __name__ == "__main__":
    result_check_data = [{'param': [1, 2, 3, 3], 'result': True}, {
        'param': [1, 2, 3, 4], 'result': False}]

    testobj = TestResult(result_check_data)
    testobj.test_all_scenarios(find_duplicate1)
    testobj.test_all_scenarios(find_duplicate2)
