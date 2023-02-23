word=["vishal","vishu","mehul","divyang","govind","veerbhadra"]

longest=0
for words in word:
    if len(words)>longest:
        longest =len(words)

print(longest)