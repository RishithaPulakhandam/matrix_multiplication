# Function to read matrices from a file
def read_matrices_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
    matrix_blocks = content.split('\n\n')
    matrix_pairs = []
    for block in matrix_blocks:
        lines = block.split('\n')
        n = int(lines[0])
        a = [list(map(int, line.split())) for line in lines[1:n+1]]
        b = [list(map(int, line.split())) for line in lines[n+1:2*n+1]]
        matrix_pairs.append((n, a, b))
    return matrix_pairs


# Function to check if a number is a power of two
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


# Function to multiply two matrices ordinarily
def matrix_multiply(a, b):
    # Check if matrices are compatible for multiplication
    if len(a[0]) != len(b):
        raise ValueError("Matrices are not compatible for multiplication")

    # Initialize result matrix with zeros
    result_matrix = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    operation_count = 0  # to count multiplication operations used in ordinary matrix multiplication

    # Perform matrix multiplication
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result_matrix[i][j] += a[i][k] * b[k][j]
                operation_count += 1  # One multiplication
    return result_matrix, operation_count


# STRASSEN MULTIPLICATION

# Add the matrices
def add_matrices(a, b):
    n = len(a)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = a[i][j] + b[i][j]
    return result


# Subtract the matrices
def subtract_matrices(a, b):
    n = len(a)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = a[i][j] - b[i][j]
    return result

#Split the matrices
def split_matrix(a):
    n = len(a)
    mid = n // 2
    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    top_right = [[a[i][j] for j in range(mid, n)] for i in range(mid)]
    bottom_left = [[a[i][j] for j in range(mid)] for i in range(mid, n)]
    bottom_right = [[a[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return top_left, top_right, bottom_left, bottom_right

#Join the matrices
def join_matrices(top_left, top_right, bottom_left, bottom_right):
    n = len(top_left)
    result = [[0 for _ in range(2 * n)] for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = top_left[i][j]
            result[i][j + n] = top_right[i][j]
            result[i + n][j] = bottom_left[i][j]
            result[i + n][j + n] = bottom_right[i][j]
    return result

#Strassen multipy
def strassen_multiply(a, b):
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]], 1 # Base case: 1 multiplication

    # Split matrices into quadrants
    A11, A12, A21, A22 = split_matrix(a)
    B11, B12, B21, B22 = split_matrix(b)

    # Strassen's algorithm
    M1, ops1 = strassen_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    M2, ops2 = strassen_multiply(add_matrices(A21, A22), B11)
    M3, ops3 = strassen_multiply(A11, subtract_matrices(B12, B22))
    M4, ops4 = strassen_multiply(A22, subtract_matrices(B21, B11))
    M5, ops5 = strassen_multiply(add_matrices(A11, A12), B22)
    M6, ops6 = strassen_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7, ops7 = strassen_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))

    # Combinations
    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)

    total_multiplications = ops1 + ops2 + ops3 + ops4 + ops5 + ops6 + ops7 # sum of all the multiplication in each equation to perform Strassen's multiplication
    # Combine sub-matrices to form the result matrix
    return join_matrices(C11, C12, C21, C22), total_multiplications


# Main function to execute the program
import time
# Main function to execute the program
def main():
    # Prompt the user to enter the input and output file paths
    input_filename = input ("Enter the input file location:")
    output_filename = input ("Enter output file location:")

    # Read the pairs of matrices from the input file
    matrices = read_matrices_from_file(input_filename)

    # Open the output file for writing the results
    with open(output_filename, 'w') as output_file:
        for i, (n, A, B) in enumerate(matrices, start=1):
            output_file.write(f"Matrix Pair {i}:\n")
            output_file.write(f"Dimensions: {n}x{n}\n")

            # Check if matrices A and B can be used in Strassen's multiplication
            if not (len(A) == len(A[0]) == len(B) == len(B[0])):
                output_file.write("Error Incorrect Matrices or not fit for matrix multiplication.\n\n")
                continue

            # Ordinary Multiplication Timing
            start_time = time.time()
            ordinary_result,ordinary_ops = matrix_multiply(A, B)
            ordinary_time = time.time() - start_time

            # Write Ordinary Multiplication Result
            output_file.write(f"Ordinary Multiplication Result (Time: {ordinary_time:.6f} seconds):\n")
            for row in ordinary_result:
                output_file.write(' '.join(map(str, row)) + '\n')
                # ordinary matrix multiplication is done if the basic requirements are met, even if the matrices are not power of two.
            output_file.write(f"Total Multiplications: {ordinary_ops}\n\n")

            # Check if matrices are of size that is a power of two
            if not is_power_of_two(n) or not is_power_of_two(len(A[0])) or not is_power_of_two(len(B)):
                # error message is shown if the matrix is not a power of two
                output_file.write("Strassen matrix multiplication cannot be performed for Matrices dimensions that are not powers of two.\n\n")
                continue  # Skip to the next pair of matrices

            # Strassen's Multiplication Timing, if applicable
            if is_power_of_two(n) and n == len(A) == len(B):
                start_time = time.time()
                strassen_result, total_multiplications = strassen_multiply(A, B)
                strassen_time = time.time() - start_time

                # Write Strassen's Multiplication Result
                output_file.write(f"Strassen's Multiplication Result (Time: {strassen_time:.6f} seconds):\n")
                for row in strassen_result:
                    output_file.write(' '.join(map(str, row)) + '\n')
                output_file.write(f"Total Multiplications (Strassen's): {total_multiplications}\n\n")
            else:
                output_file.write(f"Matrix Pair {i} Strassen's Multiplication not applicable due to non-power of two dimensions.\n\n")
    # Inform that the process is complete and the results are written to the output file
    print(f"The Matrix Multiplication results and timings have been written to {output_filename}")

# Call the main function to run the program
main()
