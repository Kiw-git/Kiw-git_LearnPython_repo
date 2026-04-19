# Try not to use the word max as it is a built-in function in python already.
def find_maximum(list):
    maximum = 0
    for number in list:
        if maximum <= number:
            maximum = number
    return maximum