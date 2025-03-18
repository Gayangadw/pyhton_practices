from multiprocessing import pool

def f(x):
    return x*x


if __name__ == "__main__":
    with pool(5) as p: