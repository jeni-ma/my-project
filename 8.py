def split_and_join(line):
    # Split the string by spaces
    words = line.split(" ")
    
    # Join the words back together using a hyphen
    result = "-".join(words)
    
    return result