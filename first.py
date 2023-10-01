# Введення рядка слів користувачем 
stringWords = str(input('Введіть рядок слів кирилицею розділених пробілами: '))
# Розділення рядка на слова та формуємо з них список
words = stringWords.split()
# Задаємо змінні для зберігання слова і кількість літер 'а' в ньому
wordMaxA = ' '
countA = 0
# Перевіряємо кожне слово на кількість 'а' (кирилиця!!!)
for word in words:
    aCount = word.count('а')
    if aCount > countA:
        countA = aCount 
        wordMaxA = word 

# Виведення слова з максимальною кількістю 'а'
if wordMaxA:
    print('Слово з найбільшою кількістю а: ', wordMaxA)
else:
    print('В рядку немає слів з літерою а!')