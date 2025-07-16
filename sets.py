fruits = {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'mango', 'nectarine', 'orange'}

fruits.add('papaya')
fruits.remove('banana')
fruits.discard('kiwi')  # This won't raise an error if 'kiwi' is not present
fruits.update(['quince', 'raspberry'])

print("Fruits set after modifications:", fruits) 