fruits = ["apple", "banana", "cherry"]
it = iter(fruits)

print(next(it)) # apple
print(next(it)) # banana

#for loop in iterators
for x in fruits:
    print(x)


#class in iterators
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 3:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_iter = iter(MyNumbers())
for x in my_iter:
    print(x)

#generators
def my_generator():
    yield "First"
    yield "Second"
    yield "Third"

gen = my_generator()
print(next(gen)) # First
