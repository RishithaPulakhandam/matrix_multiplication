# Matrix Multiplication Programming

This programming project includes a script for performing matrix multiplication in two ways: ordinary matrix multiplication and Strassen's matrix multiplication algorithm (matrix_multiplication.py). It is designed to work with square matrices where the dimension is a power of two, especially for Strassen's algorithm.I have submitted an analysis file (Programming_Assignment_Analysis_Rishitha_Pulakhandam.pdf),the original input file (LabStrassenInput.txt), given matrices in the assignment. The output for the original input (MatrixMultiplicationResults.txt), the test input file with self generated matrices that also contains matrices with errors (test_input.txt).The output for the self generated matrices (test_output.txt) 

## Features

- Reads pairs of matrices from a specified input file.
- Validates matrix dimensions to ensure compatibility for multiplication.
- Performs ordinary matrix multiplication and Strassen's matrix multiplication (when applicable).
- Outputs the results, computation time and number of operations for each multiplication method to the specified file.


## Requirements

- Python 3.x

## Usage

1. **Prepare the Input File**: Create an input text file containing pairs of matrices. Each pair should be separated by an empty line. The first line before each matrix pair should indicate the dimension (`n`) of the matrices, followed by `n` lines for each matrix in the pair (matrix a and matrix b). For example:

    ```
    2
    1 2
    3 4
    5 6
    7 8
    ```

2. **Run the Script**: Execute the script by specifying the input and output file paths directly in the script.


3. **Review the Output**: Check the specified output file for the results of the matrix multiplications and their computation times.

## Functions
### `read_matrices_from_file(filename)`

- **Purpose:** Reads matrices from a file specified by the `filename`.
- **Parameters:**
  - `filename`: The path to the input file containing matrices.
- **Returns:** A list of tuples, where each tuple contains three elements: the size `n`, matrix `A`, and matrix `B`.

### `is_power_of_two(n)`

- **Purpose:** Checks if a given number `n` is a power of two.
- **Parameters:**
  - `n`: The number to be checked.
- **Returns:** `True` if `n` is a power of two, otherwise `False`.
### `matrix_multiply(a, b)`

- **Purpose:** Performs matrix multiplication using the ordinary method.
- **Parameters:**
  - `a`: The first matrix.
  - `b`: The second matrix.
- **Returns:** A tuple containing the result matrix and the total number of operations (multiplications and additions).
### `add_matrices(a, b)`

- **Purpose:** Adds two matrices element-wise.
- **Parameters:**
  - `a`: The first matrix.
  - `b`: The second matrix.
- **Returns:** The result of the addition operation.

---

### `subtract_matrices(a, b)`

- **Purpose:** Subtracts one matrix from another element-wise.
- **Parameters:**
  - `a`: The matrix from which `b` is subtracted.
  - `b`: The matrix to be subtracted.
- **Returns:** The result of the subtraction operation.

---

### `split_matrix(a)`

- **Purpose:** Splits a given matrix into four quadrants.
- **Parameters:**
  - `a`: The matrix to be split.
- **Returns:** Four sub-matrices representing the quadrants of the input matrix.

---

### `join_matrices(top_left, top_right, bottom_left, bottom_right)`

- **Purpose:** Combines four sub-matrices into a single matrix.
- **Parameters:**
  - `top_left`, `top_right`, `bottom_left`, `bottom_right`: The four sub-matrices to be combined.
- **Returns:** The combined matrix formed by concatenating the sub-matrices.

---

### `strassen_multiply(a, b)`

- **Purpose:** Performs matrix multiplication using Strassen's algorithm.
- **Parameters:**
  - `a`: The first matrix.
  - `b`: The second matrix.
- **Returns:** A tuple containing the result matrix, the total number of multiplications, and the total number of additions/subtractions.

---

### `main()`

- **Purpose:** The main function to execute the program.
- **Input:** It prompts the user to enter the input and output file locations in the command line.
- **Example:**/Users/rishithapulakhandam/Documents/Algo/pythonProject/LabStrassenInput.txt
- **Output:** Writes the results of matrix multiplication (both ordinary and Strassen's) to the specified output file.Open in text editor to view results.

## Note

This script checks if the dimensions of the matrices are powers of two, as required for Strassen's algorithm. If matrices do not meet this criterion, an appropriate message is included in the output file.Ordinary matrix multiplication is performed if rows of a matrix is equal to the number of columns for the other. The program shows the number of multiplication operations for both normal multiplication and Strassen's multiplication.

---
## Author
Rishitha Pulakhandam <br>
rpulakh1@jh.edu

