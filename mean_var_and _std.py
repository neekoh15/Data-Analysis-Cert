//You can use this code as guidance but DO NOT COPY/PASTE IT into your proyect, this code has copyrights

import numpy as np


def calculate(lista):
  if len(lista) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
      calculations = dict()
      nparray = np.array(lista).reshape(3,3)
      calculations['mean'] = [list(np.mean(nparray, axis=0)),list(np.mean(nparray, axis=1)), nparray.flatten().mean()]
      calculations['variance'] = [list(np.var(nparray, axis=0)),list(np.var(nparray, axis=1)), nparray.flatten().var()]
      calculations['standar desviation'] = [list(np.std(nparray, axis=0)),list(np.std(nparray, axis=1)), nparray.flatten().std()]
      calculations['max'] = [list(np.max(nparray, axis=0)),list(np.max(nparray, axis=1)), nparray.flatten().max()]
      calculations['min'] = [list(np.min(nparray, axis=0)),list(np.min(nparray, axis=1)), nparray.flatten().min()]
      calculations['sum'] = [list(np.sum(nparray, axis=0)),list(np.sum(nparray, axis=1)), nparray.flatten().sum()]
      return calculations
    
calculate([9,1,5,3,3,3,2,9,0])
