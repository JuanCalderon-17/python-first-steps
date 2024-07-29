
#Here it shows how a list it's not an iterable but i can convert it into one 
nums = [1 , 2, 3]
i_nums = iter(nums)

print(i_nums)
print('--------------')

item = input()
while True:
    try:
        item.next(i_nums)
        print(item)
    except StopIteration:
        break



#Practing creatin manually the a 'range' function, it needs a next and iter 
#to make the object an iterator 
class MyRange:
    
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value 
        self.value += 1
        return current
        
nums = MyRange(1, 10)

print(next(nums)) #result = 1
print(next(nums)) #result = 2
print(next(nums)) #result = 3



#Now here i practice a generator, which are iterator but the iter and next method are created automactly
#with that said, we now they are simpler to use and are usually more common 

def my_range(start, end):
    current = start 
    while current < end:
        yield current 
        current += 1
    
nums = my_range(1, 10)
print(next(nums)) #result = 1
print(next(nums)) #result = 2
print(next(nums)) #result = 3

