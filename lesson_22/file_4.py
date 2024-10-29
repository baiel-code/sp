def get(input_list):
    unique_elements = set(input_list)
    unique_list = list(unique_elements)
    unique_list.sort()
    return unique_list
input_list = [3, 1, 2, 3, 4, 2, 5, 1]
sorted_unique_elements = get(input_list)
print(sorted_unique_elements)

numbers = [1,12,3,45,3,5,54]
print(sorted(set(numbers)))
n = [2,3,4]
a = sum(n)
print(a)