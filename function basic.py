def scream(text):
    num_of_characters = len(text)
    result = text + '!' * (num_of_characters // 4)
    print(result)


scream('you are doing great'.upper())
scream("Don't forget to ask hello".upper())
scream("Don't repeat yourself. Keep things DRY".upper())

# DOES THE SAME AS CODE ON TOP ---------
# praise = 'you are doing great'.upper()
# num_of_characters = len(praise)
# result = praise + '!'* (num_of_characters // 2)
# print(result)

# advice = "Don't forget to ask hello".upper()
# num_of_characters = len(advice)
# result = advice + '!'* num_of_characters
# print(result)


# advice2 = "Don't repeat yourself. Keep things DRY".upper()
# num_of_characters = len(advice2)
# result = advice2 + '!' * num_of_characters
# print(result)
