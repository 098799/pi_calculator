"""You have a calculator with two buttons: add 1 and divide by 2. How many times do you have to click at most to get pi aproximated to nth digit?
"""

pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862"

how_many_digits = 16  # won't work for more due to float limitation, a special library is needed for this.

def two_to(n):
    return int(float(pi)*2**n)

def power_of_two(how_many_digits):
    for j in range(5, len(pi)):
        our_number = two_to(j)
        our_binary_number = str(bin(our_number))
        calculator = 0
        for digit in our_binary_number[-1:1:-1]:
            calculator += float(digit)
            calculator = calculator / 2
        if str(4*calculator)[:how_many_digits+1] == pi[:how_many_digits+1]:
            return j, our_binary_number, 4*calculator

power, binary, score = power_of_two(how_many_digits)
        
one_clicks = 0
for digit in binary[2:]:
    one_clicks += int(digit)

how_many_times_has_calculator_been_clicked = power + one_clicks
print("How many times has calculator been clicked?", how_many_times_has_calculator_been_clicked)
print("Just to prove:")
print(pi[:how_many_digits+1])
print(score)
