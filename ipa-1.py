'''Individual Programming Assignment 1

20 points

This assignment will develop your basic familiarity with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    5 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.

    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #gross pay after taxes
    after_tax_pay = int(gross_pay * (1-tax_rate))
    #subtract expenses from after-tax pay
    Savings = after_tax_pay - expenses
    
    return Savings
    
def interest(principal, rate, periods):
    '''Interest.
    5 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time).
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    quantity = rate * periods
    simple_interest = principal * quantity
    final_value = int(principal + simple_interest)

    return final_value
    
def body_mass_index(weight, height):
    '''Body Mass Index.
    5 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.

    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    We have not yet discussed lists, but use the skills you developed
        in the command line exercise. How would you learn how to work with
        lists?

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    #convert first before computing the BMI
    weight_in_kg = weight * 0.453592
    [feet, inches] = height
    #express in inches then convert to meters
    total_inches = (feet * 12) + inches
    height_in_m = total_inches * 0.0254
    #BMI Calculation
    BMI = weight_in_kg / height_in_m **2

    return BMI