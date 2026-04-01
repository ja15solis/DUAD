string_test = "I love Traveling"

def count_upper_low_cases(text):
    if not isinstance(text, str):
        raise TypeError
    upper_cases = 0
    lower_cases = 0

    for value in text.replace(" ",""): #replace to remove spaces 
        if value.isupper():
            upper_cases += 1
        else:
            lower_cases += 1
    return {"upper_cases":upper_cases,"lower_cases":lower_cases}


result = count_upper_low_cases(string_test)
print( f"There are {result["upper_cases"]} upper cases and {result["lower_cases"]} lower cases")
