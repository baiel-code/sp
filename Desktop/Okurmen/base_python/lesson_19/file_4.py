def get_totial(numbers,issum=True):
    def get_sum():
        total =0 
        for n in numbers:
            total += n
        return total 
    
    def get_multiple():
        total = 1
        for n in numbers:
            total *= n
        return total 
    
    if issum:
        return get_sum
    return get_multiple
f_1 = get_totial([1,2,3,4,5])
f_2 = get_totial([1,2,3,4,5],issum= False)
print(f_1())
print(f_2())
