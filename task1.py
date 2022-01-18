def city(name,**kwargs):
    print(f'{name}')
    for k in kwargs:
       print(f'{k} - {kwargs[k]}')


city(name='Bishkek', population = '6 636 803', have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])