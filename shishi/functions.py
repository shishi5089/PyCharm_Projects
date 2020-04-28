from math import floor, sqrt, ceil, factorial

num = 10
print (10**0.05)
print ('Sqrt is ',sqrt(num))
print ('Power is ', pow(2,5))
print ('Ceiling is ', ceil(8.25))
print ('Floor is ', floor(8.999))
print ('Normal Round ', round(8.6353))
print ('Factorial of 5 is ', factorial(5))

rounded = floor(8.5478)
# gives back === returns
print (rounded)
result = rounded**2
print(result)


res = floor(7.85) * pow(2, 0.8) / sqrt(10.34)
print(res)

x = "10"
y = "12.88"

print(int(x) * float(y))

sentence = "The quick brown fox jumped over the lazy dog"
print(sentence.upper())
print(sentence.lower())
upper_cased = sentence.upper()
print(upper_cased * 5)
print(sentence + upper_cased)
# join the sentences
print(sentence.capitalize())


new_sentence = sentence.replace("fox" ,  "rabbit")
print(new_sentence)
# chaining functions === saves a lot of lines
new_sentence2 = sentence.lower().replace("lazy" , "super lazy").capitalize().replace("brown", "grey").isdecimal()
print(new_sentence2)

