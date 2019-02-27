def lohit(dictionary):
    for key, val in dictionary.items():

        print(f'I know this a {key} programing and this is {val}, a framework of {key}')

lohit_pgram={}

while True:
    lohit_name = input('enter name of programing:')
    lohit_frame= input('Enter the name of frame work:')
    lohit_pgram[lohit_name]=[lohit_frame]

    another=input('add another program?(y/n)')
    if another =='y':
        continue
    else:
        break
lohit(lohit_pgram)
