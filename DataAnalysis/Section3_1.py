"""
    Some case when study the book about the DataAnsys
    This section is based on the section 3.1 about Data structure and sequence
"""

"""
    Part01: tuple ：元组
"""
import bisect


def tup():
    tup = 4, 5, 6  # create the tuple
    print('The first way to create the tuple,\r\n tup = ', tup)  # printf the result

    nested_tup = (4, 5, 6), (7, 8)  # create a more complex tuple
    print('A more complex tuple,\r\n nested_tup = ', nested_tup)  # printf the result

    list = [4, 0, 2]  # create a list
    list_tup = tuple(list)  # change list to tuple by using tuple function
    print('Using tuple function, you can change a list ', list, 'to a tup', list_tup)  # printf the result

    string = 'string'  # create a string
    string_tup = tuple(string)  # change string to tuple by using tuple function
    print('Using tuple function, we can change a string', string, 'to a tup', string_tup)  # printf the result

    # Get the tuple by index
    string_tup_0 = string_tup[0]
    print('the first value about the string_tup', string_tup_0)  # printf the result

    # Modify the internal elements about the tuple
    tup_list = tuple \
        (['string', [1, 2, 3], True])  # create the tuple by using tuple function, including string,list and bool
    print('the tup_list is ', tup_list)  # printf the value

    tup_list_1 = tup_list[1].append(5)  # add an elements to the list which is in the tuple
    print('After add an element in the tuple is list, the result is', tup_list)  # printf the result

    # Connect the tuples by using '+'
    tup_list = (4, None, 'foo') + (6, 0) + ('bar',) + ([1, 2, 3, 4, 8],)  # create a tuple by using +
    print('a new tuple created by using + is ', tup_list)  # printf the result

    # Copy the tuples
    tup_list = tup_list * 4
    print('After copy ,the result is ', tup_list)  # printf the result

    # tuple unpacking
    tup = (4, 5, 6)  # create a tuple
    a, b, c = tup  # unpack the tuple
    print('The element in the tuple is ', a, b, c)  # printf the result
    tup = 2, 3, (4, 5, 6)
    a, b, (c, d, e) = tup
    print('The element in the tup is ', a, b, c, d, e)
    # common scenario for unpacking is to traverse a sequence of tuples or lists
    seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    for a, b, c in seq:
        print('a={0},b={1},c={2}'.format(a, b, c))

    # use *rest the unpack the tuple
    values = 1, 2, 3, 4, 5,
    a, b, *rest = values
    print('a={0},b={1},rest={2}'.format(a, b, rest))
    # Use underscores (_) to indicate unwanted variables
    a, b, *_ = values
    print('a={0},b={1}'.format(a, b, ))


"""
    Part02: list ：列表
"""


def List():
    a_list = [2, 3, 7, None]  # create a list
    tup = ('foo', 'bar', 'baz')  # create a tuple
    b_list = list(tup)  # change tup to list by using list function
    print('b_list={0}'.format(b_list))  # create the result
    b_list[1] = 'peekaboo'  # change the element about the second element
    print('b_list={0}'.format(b_list))  # create the result

    # some methods can be used in list
    b_list.append('dwarf')  # add an element to the end of the list
    print('b_list={0}'.format(b_list))  # create the result

    b_list.insert(1, 'red')  # insert the element to the specified list position. Computationally more expensive
    print('b_list={0}'.format(b_list))  # create the result

    b_list.pop(2)  # remove the element at a specific position and return
    print('b_list={0}'.format(b_list))  # create the result

    # The element can be removed by the remove method,
    # which will locate the first value that meets the requirements and remove it
    b_list.remove('dwarf')
    print('b_list={0}'.format(b_list))  # create the result

    print('list={0}'.format([4, None, 'foo'] + [7, 8, (2, 3)]))  # two lists can be connected using +

    b_list.extend([8, 9, (2, 3), ('fjo')])  # Use the extend method to add multiple elements to the list
    print('b_list={0}'.format(b_list))  # create the result

    a = [7, 2, 5, 1, 3]
    a.sort()
    print('a={0}'.format(a))

    c = [1, 2, 2, 2, 3, 4, 7]

    print('bisect.bisect(c,2)={0}'.format(bisect.bisect(c, 2)))
    print('bisect.bisect(c,5)={0}'.format(bisect.bisect(c, 5)))
    print('bisect.bisect(c,6)={0}'.format(bisect.bisect(c, 6)))
    print('c={0}'.format(c))
    print('bisect.insort(c,6)={0}'.format(bisect.insort(c, 6)))
    print('c={0}'.format(c))

    # Slice
    seq = [7, 2, 3, 7, 5, 6, 0, 1]
    print('seq={0}'.format(seq))
    print('seq[1:5]={0}'.format(seq[1:5]))
    seq[3:4] = [6, 3]
    print('seq={0}'.format(seq))
    print('seq[:5]={0}'.format(seq[:5]))
    print('seq[-4:]={0}'.format(seq[-4:]))
    print('seq[::2]={0}'.format(seq[::2]))
    print('seq[::-1]={0}'.format(seq[::-1]))
    # 内建序列函数
    # emumerate 用于遍历一个序列，返回i和value 其中i是索引，value为对应的值
    some_list = ['foo', 'bar', 'baz']
    mapping = {}
    for i, v in enumerate(some_list):
        mapping[v] = i
        print('mapping = {0}'.format(mapping))
    # sorted
    print('排列后的数据为{0}'.format(sorted('horse race')))

    # Zip
    print('Zip result is {0}'.format(list(zip(['foo', 'bar', 'baz'], ['one', 'two', 'three'], [False, True]))))
    for i, (a, b) in enumerate(zip(['foo', 'bar', 'baz'], ['one', 'two', 'three'])):
        print('{0}:{1},{2}'.format(i, a, b))
    # reversed 将序列中的元素倒叙排列
    print(list(sorted(range(10))))
    print(list(reversed(range(10))))


"""
    Part02: dict ：列表，又称哈希表或者关联数组
"""


def Dict():
    dict1 = {'a': 'some value', 'b': '[1,2,3,4]','d':'other values','e':'values'}  # create a dictionary
    print('dict = {0}'.format(dict1))  # printf the result

    # insert one element to an exited dictionary
    dict1['c'] = ('a', 'b', 'c', 'd')
    print('after added, dict ={0}'.format(dict1))
    # index the values in the dictionary by key value
    print('dict1_b= {0}'.format(dict1['b']))

    # Del the value by del method
    del dict1['c']
    print('dict = {0}'.format(dict1))
    # del the value by pop method
    ret = dict1.pop('b')
    print('ret = {0},dict={1}'.format(ret, dict1))
    # printf the key and values
    print('key ={0},value={1}'.format(dict1.keys(),dict1.values()))

    # Merge dictionary by using update
    dict1.update({'f':'foo','e':12})
    print('dict={0}'.format(dict1))

    # Generate a dictionary from a sequence
    mapping= dict(zip(range(10),reversed(range(10))))
    print('mapping={0}'.format(mapping))
"""
    Part03: set 集合 集合是一种无序且元素唯一的容器
"""
def Set():
    print(set([2,2,2,1,3,3]))  # create set using set function
    print({2,2,2,1,2,3})       # create set using {}
    # set operations
    set_a = {1,2,3,4,5}        # create set example set_a
    set_b = {3,4,5,6,7,8}      # create set example set_b
    # The union of two sets is the union of different elements in the two sets
    set_union = set_a.union(set_b)         # union set_a and set_b by using union method
    print('set_a = {0};after union , set_union = {1}'.format(set_a,set_union))
    set_union = set_a | set_b   # union set_a and set_b by using |
    print('set_a = {0};after union , set_union = {1}'.format(set_a,set_union))

    # Use the & operator or intersection method to get the intersection
    set_intersection = set_a.intersection(set_b)    # create intersection by using intersection
    print('set_a = {0};after intersection , set_intersection = {1}'.format(set_a,set_intersection))
    set_intersection = set_a & set_b    # create intersection by using & operator
    print('set_a = {0};after intersection , set_intersection = {1}'.format(set_a,set_intersection))
    # the above method will not replace the original collection，if we should replace the original collection, you can using last method
    # 取set_a和set_b的并集，并刷新set_a
    set_a.update(set_b)
    print('after update, set_a ={0}'.format(set_a))
    set_a|=set_b
    print('after update, set_a ={0}'.format(set_a))

    # add element 10 to set_a by using add method
    set_a.add(10)
    print('after add, set_a = {0}'.format(set_a))
    # remove element from set_a by using remove method
    set_a.remove(5)
    print('after remove, set_a = {0}'.format(set_a))

    set_a.intersection_update(set_b)
    print('set_a = {0}'.format(set_a))
    set_a &= set_b
    print('set_a = {0}'.format(set_a))

    # 集合表达式
    strings = ['a','as','bat','car','dove','python']

    unique_lengths = {len(x) for x in strings}
    print(unique_lengths)

    set(map(len,strings))

def main():
    # tup()
    # List()
    # Dict()
    Set()


if __name__ == '__main__':
    main()
