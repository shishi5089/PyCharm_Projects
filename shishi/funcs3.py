def say_hi():
    """it prints hi guest"""
    print("Hi Guest")


# call a function == using a function
# say_hi()

def greet(name):
    """it greets someone by their name"""
    print("Hi ", name)


def converter(amount_ksh, rounded="No", accuracy=0):
    usd = amount_ksh / 102
    if rounded == "Yes":
        usd = round(usd, accuracy)

    print(usd, "USD")


def converter2(amount, to, accuracy=0):
    if to == "USD":
        result = amount / 102
    elif to == "GBP":
        result = amount / 143
    elif to == "UGX":
        result = amount * 36
    elif to == "ZAR":
        result = amount / 7.8
    else:
        print("We don't support that currency")

    try:
        print(round(result, accuracy))
    except:
        pass


def converter3(distance_in_metres, to ,accuracy = 0):
    if to == "dis_cm":
        final_d = distance_in_metres * 100
        print(str(distance_in_metres) , "m equals to " , str(final_d) , "cm")
    elif to =="dis_km":
        final_d = distance_in_metres/1000
        print(str(distance_in_metres) , "m equals to " , str(final_d) , "km")
    elif to == "dis_yard":
        final_d = distance_in_metres * 1.09
        print(str(distance_in_metres), "m equals to ", str(final_d) , "yards")
    elif to == "inches":
        final_d = distance_in_metres * 39.37
        print(str(distance_in_metres), "m equals to ", str(final_d) , "inches")
    else:
        print("We do not do those conversions")

# greet("Tom")
# greet("Jane")
converter(1000)
converter(2000, rounded="Yes")
converter(3000, rounded="Yes", accuracy=2)
