def area_circle(radius , rounded = False): #rounded is optional
    result = 3.142 * radius**2
    if rounded:
        result = round(result)
    print(result)

area_circle(17 , rounded=True)
area_circle(18)