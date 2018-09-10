a = {0: 'ноль', 
     1: 'один', 
     2: 'два', 
     3: 'три', 
     4: 'четыре', 
     5: 'пять', 
     6: 'шесть', 
     7: 'семь', 
     8: 'восемь', 
     9: 'девять'}


def firsttaskfivesem(x, y=''):

  b = {'bin': bin(x),
       'oct': oct(x),
       'hex': hex(x)}

  result = ['शून्यता']

  if x in a.keys():
    result.clear()
    result.append(a.get(x))
    if y in b.keys():
      result.append(b.get(y))
  else:
    print('Введите число от 0 до 9!')
  return result

print(firsttaskfivesem(0))
#print(firsttaskfivesem(0,'hex'))

if __name__ == "__main__":
  assert firsttaskfivesem(9,'hex') == ['девять','0x9'], 'функция не работает!'
  assert firsttaskfivesem(0) == ['ноль'], 'название введённого числа не совпадает с ожидаемым!'
