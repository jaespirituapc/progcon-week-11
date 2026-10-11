def computeAverage(numbers):
    """
    Compute the average of numbers in the list until a zero is encountered.
    
    This function initializes total and count to zero, then iterates through 
    the given numbers array[cite: 1]. When it encounters a zero, the loop 
    terminates early[cite: 1]. If the count of processed numbers is greater 
    than zero, it returns the floating-point average[cite: 1]. Otherwise, it 
    returns zero to prevent division errors[cite: 1].
    """
    total = 0
    count = 0
    index = 0
    
    # Loop through the array until the end is reached or a zero is hit
    while index < len(numbers) and numbers[index] != 0:
        total = total + numbers[index]
        count = count + 1
        index = index + 1
        
    # Return the computed average or zero if no numbers were processed
    if count > 0:
        return float(total) / count
    else:
        return 0.0

# Example test case execution
numbers = [22, 9, 0, 17]
print(computeAverage(numbers))