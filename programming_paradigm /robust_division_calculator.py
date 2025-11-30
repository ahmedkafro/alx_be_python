def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling.
    
    Parameters:
        numerator (str or float): The numerator of the division.
        denominator (str or float): The denominator of the division.
    
    Returns:
        str: The result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

