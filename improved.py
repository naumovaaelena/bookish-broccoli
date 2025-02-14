import matplotlib.pyplot as plt
import time

# Recursive function to compute Fibonacci numbers
def fibonacci_recursive(n):
    """
    A simple recursive function to calculate the nth Fibonacci number.
    It is inefficient for large n because it recalculates values multiple times.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Dynamic programming approach to compute Fibonacci numbers (Memoization)
def fibonacci_dynamic(n):
    """
    A more efficient function using dynamic programming with memoization.
    It stores previously computed Fibonacci numbers to avoid redundant calculations.
    """
    memo = {0: 0, 1: 1}
    
    def fib(n):
        if n not in memo:
            memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    
    return fib(n)

# Iterative approach to compute Fibonacci numbers (Efficient)
def fibonacci_iterative(n):
    """
    An iterative method to compute the nth Fibonacci number.
    This approach is much faster than the recursive one for large n.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# Function to generate the Fibonacci sequence up to the nth element
def generate_fibonacci_sequence(n, method='recursive'):
    """
    Generates a sequence of Fibonacci numbers using the chosen method.
    Options: 'recursive', 'dynamic', or 'iterative'.
    """
    sequence = []
    for i in range(n):
        if method == 'recursive':
            sequence.append(fibonacci_recursive(i))
        elif method == 'dynamic':
            sequence.append(fibonacci_dynamic(i))
        elif method == 'iterative':
            sequence.append(fibonacci_iterative(i))
    return sequence

# Function to plot the Fibonacci sequence using matplotlib
def plot_fibonacci(sequence):
    """
    Plots the Fibonacci sequence on a graph.
    The x-axis represents the index, and the y-axis represents the Fibonacci value.
    """
    plt.plot(sequence, marker='o', color='b', linestyle='-', markersize=5)
    plt.title("Fibonacci Sequence")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

# Function to time the performance of different Fibonacci methods
def time_fibonacci_method(n, method):
    """
    Times the execution of Fibonacci sequence generation for the given method.
    It returns the execution time in seconds.
    """
    start_time = time.time()
    generate_fibonacci_sequence(n, method)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Main function to run and test the Fibonacci sequence generation
def main():
    N = 30  # Number of Fibonacci numbers to generate
    methods = ['recursive', 'dynamic', 'iterative']
    
    # Loop through each method and generate Fibonacci sequences
    for method in methods:
        print(f"Using {method.capitalize()} Method:")
        sequence = generate_fibonacci_sequence(N, method)
        print(f"First {N} Fibonacci numbers ({method.capitalize()}): {sequence[:10]}...")  # Print first 10 numbers for brevity
        
        # Time the method and print execution time
        exec_time = time_fibonacci_method(N, method)
        print(f"Execution time for {method.capitalize()} method: {exec_time:.6f} seconds\n")
    
    # Plot the Fibonacci sequence using the iterative method
    fibonacci_seq_iterative = generate_fibonacci_sequence(N, method='iterative')
    plot_fibonacci(fibonacci_seq_iterative)

if __name__ == "__main__":
    main()