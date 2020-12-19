import numpy as np 



def calculate(input_list):

    calculations = {
        'mean':[],
        'variance':[],
        'standard deviation':[],
        'max':[],
        'min':[],
        'sum':[]
    }

    if len(input_list) != 9 :
      raise ValueError ('List must contain nine numbers.')

    #input_array = np.array(input_list,np.float).reshape(3,3)
    input_array = np.array(input_list).reshape(3,3)

    # indexamos los calculos en las listas del diccionario, supongo
    # supongo que más adelante se podrá hacer con pandas en vez de con 
    # diccionarios 
    
    calculations['mean'].append(input_array.mean(axis=0).tolist())
    calculations['mean'].append(input_array.mean(axis=1).tolist())
    calculations['mean'].append(input_array.mean())

    #eje 0 columnas separadas eje 1 filas, sin argumento , todos los elementos del array
    
    calculations['variance'].append(input_array.var(axis=0).tolist())
    calculations['variance'].append(input_array.var(axis=1).tolist())
    calculations['variance'].append(input_array.var())

    calculations['standard deviation'].append(input_array.std(axis=0).tolist())
    calculations['standard deviation'].append(input_array.std(axis=1).tolist())
    calculations['standard deviation'].append(input_array.std())

    calculations['max'].append(input_array.max(axis=0).tolist())
    calculations['max'].append(input_array.max(axis=1).tolist())
    calculations['max'].append(input_array.max())

    calculations['min'].append(input_array.min(axis=0).tolist())
    calculations['min'].append(input_array.min(axis=1).tolist())
    calculations['min'].append(input_array.min())

    calculations['sum'].append(input_array.sum(axis=0).tolist())
    calculations['sum'].append(input_array.sum(axis=1).tolist())
    calculations['sum'].append(input_array.sum())

    return calculations 

print(calculate([2,6,2,8,4,0,1,5,7]))
