poem = input("Введите стихотворение: ")
phrases = poem.split()
syllables = [] 

for phrase in phrases:
  count = 0
  for letter in phrase:
    if letter.lower() in "аэюеияо":
      count += 1
  syllables.append(count)

if len(set(syllables)) == 1:
  print("Парам пам-пам")
else:
  print("Пам парам")