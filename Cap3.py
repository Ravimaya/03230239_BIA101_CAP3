################################
# https://github.com/Ravimaya/03230239_BIA101_CAP3
# Ravimaya Gurung
# BBI "B"
# 03230239
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score: 480443
################################

def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def calculate_sum(lines):
    total_sum = 0
    for line in lines:
        # Find the first and last digits
        first_digit = None
        last_digit = None
        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = int(char)
                else:
                    last_digit = int(char)
                    break
        
        # If both first and last digits are found, add them to total sum
        if first_digit is not None and last_digit is not None:
            total_sum += int(str(first_digit) + str(last_digit))
    
    return total_sum

def print_solution(file_name, total_sum):
    print(f"The total sum from the given input file {file_name} is {total_sum}")

# Main function to run the solution
def main():
    file_name = "239.txt"
    lines = read_input(file_name)
    total_sum = calculate_sum(lines)
    print_solution(file_name, total_sum)

if __name__ == "__main__":
    main()
