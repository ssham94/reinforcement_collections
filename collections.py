digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
new_dict = {}

for i in range(len(digits)):
    temp_dict = {}
    temp_dict = {'en': en[i], 'fr':fr[i] }
    new_dict[i] = temp_dict

print(new_dict)