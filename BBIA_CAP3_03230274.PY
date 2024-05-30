def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines

# Function to process the input and calculate the total sum
def calculate_total(lines):
    total = 0
    for line in lines:
        line = line.strip()  # Remove any trailing whitespace, including newline characters
        first_digit = None
        last_digit = None
        
        # Find the first digit
        for char in line:
            if char.isdigit():
                first_digit = char
                break
        
        # Find the last digit
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break
        
        # Only form a number if both digits were found
        if first_digit is not None and last_digit is not None:
            num = int(first_digit + last_digit)
            total += num
    
    return total

# Function to print the solution
def print_solution(file_path):
    lines = read_input(file_path)
    total_sum = calculate_total(lines)
    print(f"The total sum of from the given input file {file_path} is {total_sum}")

# Main execution
if __name__ == "__main__":
    input_file = "274.txt"  # Replace with your actual file name
    print_solution(input_file)
