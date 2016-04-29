
def data_type(i):
  if type(i) == str:
    return len(i)
  elif i == None:
    return 'no value'
  elif type(i) == bool:
    return i
  elif type(i) == int:
    if i < 100:
      return 'less than 100'
    elif i > 100:
      return 'more than 100'
  if type(i) == list:
    if len(i)>2:
      return i[2]
      
