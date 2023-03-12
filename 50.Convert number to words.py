https://prepinsta.com/python-program/for-converting-digit-number-to-words/

ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def number_to_words(number):
    if number < 0 or number > 999:
        return "Number out of range"
    if number < 20:
        return ONES[number]
    if number < 100:
        return TENS[number // 10] + ' ' + ONES[number % 10]
    if number < 1000:
        return ONES[number // 100] + ' hundred ' + (number_to_words(number % 100) if number % 100 > 0 else '')

number = 42
number_words = number_to_words(number)

print(number_words)
