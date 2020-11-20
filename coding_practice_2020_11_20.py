#question 1
color = input('what is your favorite color? ')

print(color,'?! No way, that is my favorite color as well!')


#question 2
cans = int(input('how many cans come in a pack? '))
packs = int(input('how many packs are there? '))

total_cans = cans * packs

print('The total number of cans is ', total_cans)


#question 3
length = float(input('what is the length of the rectangular prism? '))
width = float(input('what is the width of the rectangular prism? '))
height = float(input('what is the height of the rectangular prism? '))

volume = length * width * height

print('the volume of the rectangular prism is', volume)


#question 4
print('enter "yes" if you enter a google meet and mute the teacher ')
print('enter "no" if you do not enter a google meet and mute the teacher')
choice = input('choice:')
if choice == 'yes' or 'Yes':
    print('that is probably not a good idea')
elif choice == 'no' or 'No':
    print('ok that is good') 
else:
    print('please type yes or no')


