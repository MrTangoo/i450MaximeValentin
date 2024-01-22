class StringCalculator :
    def Add(string_number):
        parts = string_number.split(";")
        sum = 0
        for part in parts:
            try:
                ValueError
                number = int(part)
            except ValueError:
                number = 0
            if number <= 1000:
                sum += number
        return sum
    
    def Multiply(numbers):
        parts = numbers.split(";")
        product = 1
        for part in parts :
            try :
                number = int(part)
            except ValueError:
                 raise ValueError("Invalid input: '{}' is not a valid number.".format(part))
            if number <= 1000 :
                product *= number
        return product


        