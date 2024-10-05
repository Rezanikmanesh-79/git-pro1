def process_string(s):
    vowels = "aeiouAEIOU" 
    result = ""  
    for char in s:
        if char not in vowels:  
            result += "." + char.lower()  

    return result
input_string = input()
output_string = process_string(input_string)
print(output_string)
