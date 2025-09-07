from utils import TestResult


def check_valid_anagram1(s: str, t: str) -> bool:
    # using hashmap or dict
    # create empaty dict ,
    # add element from s  and its  ,count increse value from 1 when duplacate occure,  store it in hashmap
    # from t check each element from hashmap and decreaese value to 1 ,store it in hasmap
    # check every value equal to zero  otherwise retrun false 
    hashmap = {}
    for i in s:
        hashmap[i] = hashmap.get(i, 0) + 1
    for i in t:
        hashmap[i] = hashmap.get(i, 0) - 1

    for i in hashmap.values():
        if i != 0:
            return False
    return True

def check_valid_anagram2(s: str, t: str) -> bool:
    # sort s and t , sorted string is equal then return true otherwise false
    # tO->  O(m × log(m) + n × log(n))
    # s) -> O(m + n)
    return len(s) == len(t) and sorted(s) == sorted(t)

def check_valid_anagram3(s: str, t: str) -> bool:
    # check frequency_array
    # create new_array of zero with 26 position 
    # position is alphabetical order e.g a =0,b=1
    # loop s element,increment position value with 1 if occure in s,
    # loop t element ,decreement poition value with 1 which occure in t
    # check values from new_array where any value present other than zero return false otherwise True
    ele_array=[0]*26
    for i in s:
        ele_array[ord(i)-ord('a')] += 1
    for j in t:
        ele_array[ord(j)-ord('a')] -= 1
    return not(any(ele_array))

if __name__ == "__main__":
    resultset = [{'params': {"s": "hello", "t": "world"}, "result": False}, 
                 {'params': {"s": "helo", "t": "lohe"}, "result": True}]
    TestResult(resultset).test_all_scenarios(check_valid_anagram1)
    TestResult(resultset).test_all_scenarios(check_valid_anagram2)
    TestResult(resultset).test_all_scenarios(check_valid_anagram3)
