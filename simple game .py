import string
from collections import Counter

# a şıkı
def remove_stop_words(input_list):
    stop_words = {'a', 'an', 'the'}
    punctuation_symbols = set(string.punctuation)

    result_list = []
    for word in input_list:
        
        cleaned_word = ''.join(char for char in word if char not in punctuation_symbols)
        
        if cleaned_word and cleaned_word.lower() not in stop_words:
            result_list.append(cleaned_word)

    return result_list

# b şıkı
def word_frequency_dictionary(word_list):
    return dict(Counter(word_list))
    
# c şıkı
def remove_duplicates_from_dict(word_dict):
    unique_words = list(word_dict.keys())
    return unique_words

# d şıkı
def create_grams(liste):
    if len(liste) < 3:
        return [liste]  

    result_grams = [liste[i:i+3] for i in range(0, len(liste), 3) if i+2 < len(liste)]
    
    if len(liste) % 3 == 2:
        result_grams.append(liste[-2:])
    else:
        result_grams.append(liste[-1:])
        
    return result_grams
#$####################

original_list = input("Enter a text ")
print("Original list:")
print(original_list)
original_listt = original_list.split()

########################################
resulting_list = remove_stop_words(original_listt)
print("\nA) Resulting list:")
print(resulting_list)

####################
resulting_dict = word_frequency_dictionary(resulting_list)
print("\nB) Resulting dictionary:")
print(resulting_dict)

########################################
resulting_remo = remove_duplicates_from_dict(resulting_dict)
print("\nC) Resulting removed:")
print(resulting_remo)

####################
resulting_grams = create_grams(resulting_remo)
print("\nD) Resulting grams:")
print(resulting_grams)