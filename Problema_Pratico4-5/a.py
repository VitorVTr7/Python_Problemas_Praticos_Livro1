'''
Suponha que as variaveis primeiro, ultimo, rua, numero, cidade, estado, codPostal
ja tenham sido atribuitodas.
Escreva uma instrucao print que crie uma etiqueta de correspondencia:

John Doe
123 Main Street
AnyCity, AS 09876
'''

primeiro = 'Jonh'
ultimo = 'Doe'
rua = 'Main Street'
numero = 123
cidade = 'AnyCity'
estado = 'AS'
codPostal = '09876'

print('{} {}\n{} {}\n{}, {} {}'.format(primeiro, ultimo, numero, rua, cidade, estado, codPostal))
