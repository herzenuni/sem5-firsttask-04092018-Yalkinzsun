import time

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

class RangeException(Exception):
  pass

def firsttaskfivesem(x, y=''):
  """

  """
  start_time = time.ctime(time.time())
  logger = []
  logger.append("Время и дата запуска функции: " + start_time)
  
  b = {'bin': bin(x),
       'oct': oct(x),
       'hex': hex(x)}

  result = ['शून्यता']
    
  if x in a.keys():
    result.clear()
    result.append(a.get(x))
    if y in b.keys():
        result.append(b.get(y))
    elif y != '':
        print('Выбирите систему счисления: hex, bin или oct!')
        logger.append("Исключения: ConvertTypeException")
      
  else:
#    raise RangeException('Введите число от 0 до 9!')
     print('Введите число от 0 до 9!')
     logger.append("Исключения: RangeException")

  if len(logger) == 1:   
     logger.append("Исключения: не выявлено!")

  with open('newfile.txt', 'a') as f:
   f.write(str(logger) + "\n")
  return result

def tests():
  assert firsttaskfivesem(9,'hex') == ['девять','0x9'], 'функция не работает!'
  assert firsttaskfivesem(0) == ['ноль'], 'название введённого числа не совпадает с ожидаемым!'

if __name__ == "__main__":
  x = int(input('Введите первый аргумент:'))
  y = input('Введите второй аргумент(а можете и не вводить):')
 # tests()
  print(firsttaskfivesem(x,y))
