def check_palindrome(word):
	letters = list(word.lower())
	for i in letters:
		j = letters.index(i) + 1
		if i == letters[-j]:
			pass
		else: 
			return False
	return True

def palindrome_two(word):
	letters = list(word.lower())
	letter_dict = {a+b:True for a, b in zip(letters, letters[::-1]) if a == b}
	return True if len(letter_dict) == (len(letters)/2) else False
	

def palindrome_three(word):
	a = list(word.lower())
	b = a[::-1]
	return True if a == b else False
			
		
words = ['hannah', 'Hannah', 'alanna']
for word in words:
	print(word), ':', check_palindrome(word)
	print(word), ':', palindrome_two(word)
	print(word), ':', palindrome_three(word)






