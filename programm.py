print('Программа "Инициалы".')
while True:
  print('Введите свое полное имя:')
  name = input()
  name = name.title()
  alphabit = ''
  for i in range(1040, 1072):
    alphabit += chr(i)
  num = 0
  name2 = ''
  for c in name:
    if c in alphabit:
      num += 1
      name2 += c
  if num != 3:
    print('Введите верное имя!')
    continue
  else:
    print(f'Ваши инциалы: {name2}')
  flag = True
  while True:
    print('Вы хотите продолжить? (введите да/нет)')
    word = input()
    if word.lower() == 'да':
      break
    elif word.lower() == 'нет':
      flag = False
      break
    else:
      print('Введите корректный ответ')
  if flag == False:
     break
 print('Программа закрыта.')
