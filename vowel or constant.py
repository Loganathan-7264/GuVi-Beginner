b = input("Input a letter of the alphabet: ")

if b in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % b)
elif b == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % b) 
