disordered_string = "javier-solis-prieto-ingeniero"

def order_string(text):
    string_list = text.split("-")
    string_list.sort()
    ordered_text = ""
    for index,value in enumerate(string_list):
        if index == len(string_list)-1:
            ordered_text += value
            continue
        else:
            ordered_text += value + "-"
    return ordered_text

print(order_string(disordered_string))