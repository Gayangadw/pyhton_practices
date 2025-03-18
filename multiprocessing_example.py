import multiprocessing
import time

number_of_processes = 5
number_of_iterations = 5

N = 99999999

def sum_all_numbers(n):
    total_sum = sum(range(n + 1))
    return total_sum

def print_sum(n):
    print("Sum:", sum_all_numbers(n))

def without_multiprocessing():
    print("Start the Without Multiprocessing!")
    
    for i in range(number_of_iterations):
        result = sum_all_numbers(N)
        print("Sum:", result)

def with_multiprocessing():
    print("Start With Multiprocessing!")
    jobs = []
    
    for i in range(number_of_processes):
        process = multiprocessing.Process(
            target=print_sum,  
            args=(N,)
        )
        jobs.append(process)
        
    for j in jobs:
        j.start()
        
    for j in jobs:
        j.join()

def main():
    print("Summing all numbers between 0 and", str(N) + ".\n")
    
    start_time = time.time()
    without_multiprocessing()
    print("------- Function without multiprocessing took %s seconds ----------------\n" % round(((time.time() - start_time))),2)
    
    start_time = time.time()
    with_multiprocessing()
    print("------- Function with multiprocessing took %s seconds ----------------\n" % round((time.time() - start_time)),2)

if __name__ == "__main__":
    main()