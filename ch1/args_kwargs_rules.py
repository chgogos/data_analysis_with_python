# def f1(**kwargs, x): # SyntaxError: invalid syntax
#   print(f"{kwargs=}, {x=}")


def f2(x, y):
    print(f"{x=}, {y=}")


f2(1, 2)  # x=1, y=2
f2(x=1, y=2)  # x=1, y=2
f2(1, y=2)  # x=1, y=2
# f2(1, x=2) # TypeError: f2() got multiple values for argument 'x'
# f2(x=1, 2) # SyntaxError: positional argument follows keyword argument


def f3(x, *args, y, **kwargs):
    print(f"{x=}, {args=}, {y=}, {kwargs=}")


f3(1, 2, 3, y=4, z=5, w=6)  # x=1, args=(2, 3), y=4, kwargs={'z': 5, 'w': 6}
# f3(1, 2, 3, 4, z=5, w=6) # TypeError: f3() missing 1 required keyword-only argument: 'y'
