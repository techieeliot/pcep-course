list_of_things = [12, 'hello', 3.14, True, None, [1, 2, 3], {'key': 'value'}, (1, 2)]

# print(type(list_of_things))

car_makes = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes-Benz']
car_models = ['Camry', 'Civic', 'F-150', 'Malibu', 'Altima', '3 Series', 'C-Class']
# export car_makes, car_models
# print(car_makes[0])
# print(car_models[0])
# print(car_makes[0][-3:], car_models[0][-3:], sep='_')

for car in car_makes:
    for model in car_models:
        print(f"{car[-3:]}_{model[-3:]}")


# print("maker", car_makes[0])
# print("maker", car_makes[6])
# print("maker", car_makes[-1])

# print("maker", car_makes[-2])
# print("maker", car_makes[5])

hello = "Hello World!"

# print("7th character", hello[6])

# print("britsh", hello[1:6])

# print("scramble", hello[1:8:2])

# print("reverse", hello[::-1])

new_make_group = car_makes

new_make_group.append('Volkswagen')
# new_make_group.insert('Audi')

# print("new make group", new_make_group)

new_make_group.remove('Ford')
new_make_group.pop(2)

new_make_group.sort()

new_make_group.reverse()


print("Old car models: ", car_models)
car_models2 = car_models.copy()

car_models2.remove('Civic')
car_models2.insert(0, 'Accord')

print("Updated car models: ", car_models2)   

