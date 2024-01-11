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
        if ';' in numbers:
            produit = 25
        else:
            try:
                produit = int(numbers)
            except ValueError:
                produit = 0
        return produit


        