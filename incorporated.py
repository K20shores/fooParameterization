from foo.parameterization import Foo22, ModifiedFoo22

def do_something(foo):
    for i in range(1, 10):
        foo.compute(i)

def DoIt():
    do_something(Foo22())
    do_something(ModifiedFoo22())

if __name__ == '__main__':
    DoIt()
