import string

text = input("Podaj tekst.")
char_w_spaces = len(text)
char_without_spaces=len(text.replace(" ",""))

words = text.split()
word_count = len(words)

sentence_count = 0
for characters in words:
    if characters in ".?!":
        sentence_count += 1

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

word_frequency = {}
for word in words:
    word = word.lower()
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

max_count = max(word_frequency.values())

most_common =[]
for word, count in word_frequency.items():
    if count == max_count:
        most_common.append(word)

print("Liczba znaków ze spacjami: ", char_w_spaces)
print("Liczba znaków bez spacji: ", char_without_spaces)
print("Liczba słów: ",word_count)
print("Liczba zdań: ", sentence_count)
print("Najdluższe slowo: ", longest_word)
print("Najczęstsze słowo: ", most_common)