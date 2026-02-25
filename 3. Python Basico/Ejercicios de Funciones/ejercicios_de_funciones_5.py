string_test = "I love Traveling"

def count_upper_low_cases(text):
    upper_cases = 0
    lower_cases = 0

    for value in text.replace(" ",""): #replace to remove spaces 
        if value.isupper():
            upper_cases += 1
        else:
            lower_cases += 1

    return  f"There's {upper_cases} upper cases and {lower_cases} lower cases"


print(count_upper_low_cases(string_test))
