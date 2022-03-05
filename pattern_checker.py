def frequency_counter(sub_string, main_string, sub_length, main_length):
    result = 0
     
    for i in range(main_length - sub_length + 1):

        j = 0
        while j < sub_length:
            if (main_string[i + j] != sub_string[j]):
                break
            j += 1
 
        if (j == sub_length):
            result += 1
            j = 0
    return result



main_string = input("Enter Your Main String:  ")
sub_string = input("Enter Your Substring:  ")
sub_length = len(sub_string)
main_length = len(main_string)
print("Occurrence: ",frequency_counter(sub_string, main_string, sub_length, main_length), " times")