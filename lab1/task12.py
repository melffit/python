text = input("введите текст: ")
words = text.split()
print(f"сколько всего слов: {len(words)}")
frequencies = {}
for word in words:
    frequencies[word] = frequencies.get(word, 0) + 1
print("частота слов:")
for word, count in frequencies.items():
    print(f"  {word}: {count}")
most_common = max(frequencies, key=frequencies.get)
print(f"самое частое слово: {most_common}")
shortest = min(words, key=len)
longest = max(words, key=len)
print(f"самое короткое: {shortest}, самое длинное: {longest}")
filtered = [word for word in words if len(word) >= 3]
print(f"\nпосле удаления слов короче 3 символов:")
print(f"всего слов: {len(filtered)}")
frequencies2 = {}
for word in filtered:
    frequencies2[word] = frequencies2.get(word, 0) + 1
print("частота слов:")
for word, count in frequencies2.items():
    print(f"  {word}: {count}")
most_common2 = max(frequencies2, key=frequencies2.get)
print(f"самое частое слово: {most_common2}")
shortest2 = min(filtered, key=len)
longest2 = max(filtered, key=len)
print(f"самое короткое: {shortest2}, самое длинное: {longest2}")