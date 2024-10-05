def process_string(s):
    vowels = "aeiouAEIOU" 
    result = ""  
    for char in s:
        if char not in vowels:  
            result += "." + char.lower()  
