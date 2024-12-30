from geopy.geocoders import Nominatim
geolocator = Nominatim (user_agent = 'wazeyes')

endereco = input('Digite um endereco com número e cidade.'
                 
                 'Exemplo: avenidade paulista, 100 São Paulo: ')

resultado = str(geolocator.geocode(endereco)).split(',')

if resultado [0] != 'None':
    print('Endereço completo.: ', resultado)
    print('Bairo.............: ', resultado[1])
    print('Cidade............: ', resultado[2])
    print('Regiao...........: ', resultado[3])