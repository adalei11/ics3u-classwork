#CODING BAT
#hello_name
def hello_name(name):
   return "Hello " + name + "!"

#make_abba
def make_abba(a, b):
  return a + b*2 + a

#make_tags
def make_tags(tag, word):
  return "<"+tag+">" + word + "</"+tag+">"

#make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#extra_end
def extra_end(str):
  return str[-2:] * 3

#first_two
def first_two(str):
  if len(str) >= 2:
    return str[:2]
  else:
    return str

#first_half
def first_half(str):
  return str[:len(str)/2]

#without_end
def without_end(str):
  return str[1:-1]

#combo_string
def combo_string(a, b):
  return a+b+a if len(a)<len(b) else b+a+b

#non_start
def non_start(a, b):
  return a[1:]+b[1:]

#left2
def left2(str):
  return str[2:] + str[:2]



#PYTHON WORKBOOK
#34
num = int(input("Please enter a integer: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

#35
human_age = int(input("Input a dog's age in human years: "))

if human_age < 0:
	print("Age must be positive number.")
	exit()
elif human_age <= 2:
	dog_age = human_age * 10.5
else:
	dog_age = 21 + (human_age - 2)*4

print("The dog's age in dog's years is", dog_age)

#36
letter = input('enter a letter of the alphabet: ')

if letter == 'a' or letter == 'e' or letter == 'o' or letter == 'i' or letter == 'u':
    print('It is a vowel')
elif letter == 'y':
    print('sometimes it is a vowel and sometimes it is a consonant')
else:
    print('It is a consonant')

#37
print("Whats With That Shape\n")

sides = int(input("How many sides does your shape have?\n>>> "))

if sides <= 2:
    print("No such shape found.\nSorry Please Try Again!!")
elif sides == 3:
    print("Your three sided shape is a TRIANGLE")
elif sides == 4:
    print("Your four sided shape is a SQUARE")
elif sides == 5:
    print("Your five sided shape is a PENTAGON")
elif sides == 6:
    print("Your six sided shape is a HEXAGON")
elif sides == 7:
    print("Your seven sided shape is a HEPTAGON")
elif sides == 8:
    print("Your eight sided shape is a OCTAGON")
elif sides == 9:
    print("Your nine sided shape is a NONAGON")
elif sides == 10:
    print("Your ten sided shape is a DECAGON")    
else:
    print("A POLYGON can have an infinite number of sides.")

#38
month = input('enter the name of a month: ')
day = 31

if month =='April' or month == 'June' or month == 'September' or month == 'November':
    day == 30
elif month == 'February':
    day == '28 or 29'
else:
    day == 31

print(month, 'has', day, 'days in it.')

print("Name That Noise\n")

#39
decibel = int(input("Enter the sound level in Decibels:\n>>> "))

if decibel <= 10:
    print("Sorry I did not hear you.")    
elif decibel <= 20:
    print("I don't hear a thing. SHHH!'")
elif decibel <= 40:
    print("It's no louder than a quiet room.")
elif decibel == 70:
    print("Wake up sleepy! It's as loud as a alarm clock.")
elif decibel <= 69:
    print("Noise level is in between a quiet room and a alarm clock.")
elif decibel <= 105:
    print("Noise level is in between a alarm clock and a lawnmower")
elif decibel == 106:
    print("Stay off the grass! Don't you hear the lawnmower'")
elif decibel <= 129:
    print("Noise level is in between a lawnmower and a jackhammer.")  
elif decibel == 130:
    print("Danger Construction Zone\nExcessive noise due to jackhammer.")
elif decibel >= 150:
    print("Cover your ears. Its dangerously loud.\nEar drums rupture at 150 Db.") 
elif decibel >= 200:
    print("Welcome to the big bang.")

#41
print("The Frequencies Of Music")

c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88

name = input("Enter a note(eg. c4):\n>>> ")

note = name[0]
octave = int(name[1])

freq = -1

if note == "c" or note == "C":
    freq = 261.63
elif note  == "d" or note == "D":
    freq = 293.66
elif note == "e" or note == "E":
    freq = 329.63
elif note == "f" or note == "F":
    freq = 349.23
elif note == "g" or note == "G":
    freq = 392.00
elif note == "a" or note == "A":
    freq = 440.00
elif note == "b" or note == "B":
    freq = 493.88

freq /= 2 ** (4 - octave)

print("The frequency of", note.title(), octave, "is %.2f Hz." % freq)

#42
print("What Note Is That Frequency ?")

freq = float(input("Enter a frequency:\n>>> "))

if freq < 260.62:
    print("Frequency is out of range.")
elif freq >= 260.63 and freq <= 262.63:
    print("The note C4 has a frequency of 261.63 Hz.")
elif freq >= 292.66 and freq <= 294.66:
    print("The note D4 has a frequency of 293.66 Hz.")
elif freq >= 328.63 and freq <= 330.63:
    print("The note E4 has a frequency of 329.63 Hz.")
elif freq >= 348.23 and freq <= 350.23:
    print("The note F4 has a frequency of 349.23 Hz.")
elif freq >= 391.00 and freq <= 393.00:
    print("The note G4 has a frequency of 392.00 Hz ")
elif freq >= 439.00 and freq <= 441.00:
    print("The note A4 has a frequency of 440.00 Hz.")
elif freq >= 492.88 and freq <= 494.88:
    print("The note B4 has a frequency of 493.88 Hz.")
elif freq > 494.89:
    print("The frequency is out of range.")

#43
print("The Faces of Money\n")

money = int(input("Enter The Dollar Amount:\n>>> $"))

if money == 1:
    print("The one dollar banknote features George Washington.")
elif money == 2:
    print("The two dollar banknote features Thomas Jefferson.")    
elif money == 5:
    print("The five dollar banknote features Abraham Lincoln.")  
elif money == 10:
    print("The ten dollar banknote features Alexander Hamilton.") 
elif money == 20:
    print("The twenty dollar banknote features Andrew Jackson.")    
elif money == 50:
    print("The fifty dollar banknote features Ulysses S. Grant.")  
elif money == 100:
    print("The one hundred dollar banknote features Benjamin Franklin.")    
else:
    print("The banknote in that denomination is not available.")

#44
print("Name That Holliday")

month = str(input("Enter the month:\n>>> "))
day = int(input("Enter the day:\n>>> "))

if month == "january" and day == 1:
    print(month.title(), day, "st Happy New Years.")
elif month == "july" and day == 1:
    print(month.title(), day, "st Happy Birthday Canada.")
elif month == "december" and day == 25:
    print(month.title(), day,"th Merry Christmas.")
else:
    print("Sorry, there is NO Canadian holliday on", month.title(), day)
