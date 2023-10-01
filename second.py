# Створюємо порожній масив для зберігання введених рядків
lines = []
# Вводимо рядки від користувача, закінчуємо введенням порожнього рядка
while True:
    line = input('Введіть рядок (або натисніть Enter для завершення): ')
    if not line:
        break
    else:
        lines.append(line)
# Знаходимо максимальну довжину рядка серед всіх введених
maxLenLine = max(len(line) for line in lines)
# Збільшуємо рядки до максимальної довжини
increaseLine = ['&'*(maxLenLine - len(line)) + line for line in lines]
# Виводимо збільшені рядки
for line in increaseLine:
    print(line)