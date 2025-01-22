# Given text
text = """
the Zave crasKed Dnd hiW thH sandcastle head-on. the sandcastle began to
melt under the waYes forcH and as the wave Ueceded, half the sandcastle was
gone. the next wave hit, not quite as strong, but still managed to cover the
remains of the sandcastle and take more of it awaB. the third wave, a big Rne,
crashed over the sandcastle completely covering and engXlfing it. when it
receded, there wDs no tUacH the sandcastle ever existed and hours of hard
work disappeared forever.
he couldn't rememEer exactly whHre he hDd read it, but he was sure that he
had. the fact that she didn't believe him was quite frustratinJ as he began tR
search the internet tR finG the article. it wasn't as if it was sRmethiQg that
seemed impossiblH. yet she insisted on always seeing the source whenever he
stated a fact.
"""

# Extract the capital letters from the text
capital_letters = [char for char in text if char.isupper()]

# Caesar shift by -3 (3 backwards)
shifted_capitals = [chr(((ord(char) - ord('A') - 3) % 26) + ord('A')) for char in capital_letters]

# Replace the original capital letters with shifted ones in the text
shifted_text = list(text)  # Convert text to a list for mutability
capital_index = 0

for i, char in enumerate(shifted_text):
    if char.isupper():
        shifted_text[i] = shifted_capitals[capital_index]
        capital_index += 1

# Join the shifted letters into a string
shifted_string = ''.join(shifted_capitals)

# Convert the shifted text list back to a string
shifted_text_result = ''.join(shifted_text)

# Output the shifted string and the modified text
print(shifted_string, shifted_text_result)