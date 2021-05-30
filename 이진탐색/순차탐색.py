def squential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

array = ['Hanul', 'Jonggu', 'Dongbin','Taeil', 'Sangwook']
n = len(array)

print(squential_search(n,'Dongbin',array))