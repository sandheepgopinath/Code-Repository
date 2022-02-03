#Exponent
print(3**4)



#Multiplying Strings
a='Hello'
print(a*5)

#String comparison
print('Apele'>'Ane')

#%%
print('appld'<'apple')

print('abc'<'abca')


w='python'

print(w[-4:])



# %%

# Shorthand operators

count=1
count*=19
print(count)

print(count in [10,19,23,10])

print(10<count<15)


# %%
#Escape charachters
print('Hello \' wo\trl\nd')

# %%
#Diving a command in multiple lines

print('''Hello
World''')


print('Hello I am \
     trying to split\
        the statement into 3 lines')
# %%
text='jello-World'

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.capitalize().swapcase())


print(text.isdigit())
print(text.islower())
print(text.istitle())
print(text.isspace())
print(text.isalnum())
print('\n')
print(text.strip().isalnum())
# %%
# Strip 
text='wg sadkgh asjhg'
text=text.strip()
print(text.startswith('w'))
print(text.endswith('g'))
# %%

print(text.count('w'))
print(text.index('w'))
print(text.replace('w',''))