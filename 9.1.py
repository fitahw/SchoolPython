song_string = """Some things in life are bad
They can really make you mad
Other things just make you swear and curse
When you're chewing on life's gristle
Don't grumble, give a whistle
And this'll help things turn out for the best
And always look on the bright side of life
Always look on the light side of life
If life seems jolly rotten
There's something you've forgotten
And that's to laugh and smile and dance and sing
When you're feeling in the dumps
Don't be silly chumps
Just purse your lips and whistle, that's the thing
And always look on the bright side of life
Come on!"""

words = []
for word in song_string.split():

	if len(word) <= 4 and not 'a' in word.lower():
		words.append(word)
print(words)