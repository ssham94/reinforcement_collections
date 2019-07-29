digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
new_dict = {}

for i in range(len(digits)):
    new_dict[str(i)] = {'french': fr[i], 'en':fr[i] }

print(new_dict)