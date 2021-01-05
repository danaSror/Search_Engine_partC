import re
class WordsToNumber :
    def __init__(self):
     self.allowedStrings =[ "zero", "one", "two", "three", "four", "five", "six", "seven",
                       "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
                       "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
                       "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
                       "hundred", "thousand", "million", "millions", "billion", "trillion", "m", "bn"]

    def getNumericWords(self):
        return self.allowedStrings

    def handle_number(self,word):
        ans = ""
        if word.find(",") != -1:
            word = word.replace(",", "")
        word = float(word)
        multi = 1000
        if word >= multi:
            multi = multi * 1000
            if word >= multi:
                multi = multi * 1000
                if (word >= multi):  # is billion or trillion
                    ans = "B"
                    word = (word / multi)
                else:  # is million
                    ans = "M"
                    multi /= 1000
                    word = word / multi

            else:  # is thousand
                ans = "K"
                multi /= 1000
                word = word / multi

            word = float("{:.3f}".format(word))
        return (str(word) + ans)

    def execute(self,toConvert):
        isValidInput = True
        result = 0
        finalResult = 0
        if ( (not toConvert == None) and (len(toConvert) > 0)) :
            toConvert = toConvert.replace("-", " ")
            toConvert = toConvert.lower().replace(" and", " ")
            splittedParts = toConvert.strip().split()
            for  str in splittedParts:
                if not ((str in self.allowedStrings) == isValidInput):
                    continue
            if isValidInput:
                for str in splittedParts:
                    if str == ("zero"):
                        result += 0
                    elif str == ("one"):
                        result += 1
                    elif str ==  ("two"):
                        result += 2
                    elif str == ("three"):
                        result += 3
                    elif str == ("four"):
                        result += 4
                    elif str == ("five"):
                        result += 5
                    elif str == ("six"):
                        result += 6
                    elif str == ("seven"):
                        result += 7
                    elif str == ("eight"):
                        result += 8
                    elif str == ("nine"):
                        result += 9
                    elif str == ("ten"):
                        result += 10
                    elif str == ("eleven"):
                        result += 11
                    elif str == ("twelve"):
                        result += 12
                    elif str == ("thirteen"):
                        result += 13
                    elif str == ("fourteen"):
                        result += 14
                    elif str == ("fifteen"):
                        result += 15
                    elif str == ("sixteen"):
                        result += 16
                    elif str == ("seventeen"):
                        result += 17
                    elif str == ("eighteen"):
                        result += 18
                    elif str == ("nineteen"):
                        result += 19
                    elif str == ("twenty"):
                        result += 20
                    elif str == ("thirty"):
                        result += 30
                    elif str == ("forty"):
                        result += 40
                    elif str == ("fifty"):
                        result += 50
                    elif str == ("sixty"):
                        result += 60
                    elif str == ("seventy"):
                        result += 70
                    elif str == ("eighty"):
                        result += 80
                    elif str == ("ninety"):
                        result += 90
                    elif str == ("hundred"):
                        if result == 0:
                            result = 1
                        result *= 100
                    elif str == ("thousand"):
                        if result == 0:
                            result = 1
                        result *= 1000
                        finalResult += result
                        result = 0
                    elif str == ("million") or str == ("m") or str == ("millions"):
                        if result == 0:
                            result = 1
                        result *= 1000000
                        finalResult += result
                        result = 0
                    elif str == ("billion") or str == ("bn"):
                        if result == 0:
                            result = 1
                        result *= 1000000000
                        finalResult += result
                        result = 0
                    elif str == ("trillion"):
                        if result == 0:
                            result = 1
                        result *= 1000000000000
                        finalResult += result
                        result = 0
        finalResult = finalResult + result
        return  finalResult

