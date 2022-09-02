class RomanNumerals:

    compliance = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def to_roman(val):
        result = ''
        sVal = str(val)
        lenght = len(sVal)
        counter = 0
        while lenght != 0:
            counter += 1
            result += RomanNumerals.letterReturner(lenght, sVal[counter - 1])
            lenght -= 1

        return result

    def from_roman(roman_num):
        result = 0
        counter = 0
        skipStep = False
        for i in roman_num:
            if skipStep:
                skipStep = False
                continue
            currentDigit = RomanNumerals.compliance[i]
            try:
                nextDigit = RomanNumerals.compliance[roman_num[counter + 1]]
            except:
                result += currentDigit
                break

            if currentDigit >= nextDigit:
               result += currentDigit
            else:
                result += nextDigit - currentDigit
                skipStep = True
                counter += 1
            counter += 1
        return result




    def letterReturner(digit, number):

        number = int(number)
        if number == 0 :
            return ''

        if digit == 1:

            if number == 4:
                return 'IV'
            elif number == 9:
                return 'IX'
            elif number == 5:
                return 'V'
            elif number < 5:
                return 'I' * number
            elif number > 5:
                return 'V' + ('I' * (number - 5))

        elif digit == 2:

            if number == 4:
                return 'XL'
            elif number == 9:
                return 'XC'
            elif number == 5:
                return 'L'
            elif number < 5:
                return 'X' * number
            elif number > 5:
                return 'L' + ('X' * (number - 5))

        elif digit == 3:

            if number == 4: return 'CD'
            elif number == 9: return 'CM'
            elif number == 5: return 'D'
            elif number < 5: return 'C' * number
            elif number > 5: return 'D' + ('C' * (number - 5))

        elif digit == 4:
            return 'M' * int(number)

print(RomanNumerals.from_roman('XXI'))