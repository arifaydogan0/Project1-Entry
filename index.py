def reversed_list(l):
    l = l[::-1]
    for i in range(len(l)):
        l[i] = (l[i])[::-1]
    
    print(l) 
    
my_list = [[1, 2], [3, 4], [5, 6, 7]]
reversed_list(my_list)

flat_list = []

def flatten_func(given_list):
  for item in given_list:
        if isinstance(item, list):
            flatten_func(item)
        else:  
            flat_list.append(item)
    
    
my_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
(flatten_func(my_list))
print(flat_list)