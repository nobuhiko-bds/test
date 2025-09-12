def calculate_even_sum(numbers):
    return sum(num for num in numbers if num % 2 == 0)

def average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0

input_str = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_str.strip().split()))

even_sum = calculate_even_sum(numbers)
avg = average(numbers)

print(f"Sum of even numbers: {even_sum}")
print(f"Average of all numbers: {avg}")
