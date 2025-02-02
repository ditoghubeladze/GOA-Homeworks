def analyze_list():
    numbers = []
    for i in range(5): 
        numbers.append(int(input("Enter a number: ")))
    
    print(f"Max: {max(numbers)}, Min: {min(numbers)}, Sum: {sum(numbers)}, Length: {len(numbers)}")

analyze_list()