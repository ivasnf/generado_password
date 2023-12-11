import string 
import secrets

def contiene_mayusculas(password) -> bool:
    """verifica si un password tiene mayusculas"""

    for letra in password:
        if letra.isupper():
            return True
        
    return False #There were no tiene-mayusculas chars
    
def contiene_simbolos(password) -> bool:
    """verifica si un password tiene simbolos"""

    for letra in password:
        if letra in string.punctuation:
            return True
            
    return False # There were no tiene_mayusculas char
        
def generar_password(longitud, tiene_simbolos, tiene_mayusculas) -> str:
    """
    Genrar un password basado en las especificaciones del ususario
    :param longitud: la longitud del password
    :param tiene_simbolos: el password debe incluir simbolos
    :param tiene_mayusculas: el password debe incluir mayusculas
    :return: str
    """
    #crear una combinacion de letras y digitos para elegir
    combinacion = string.ascii_lowercase + string.digits

    #si el usuario quiere simbolos, entonces añade signos de puntuacion en al 
    #combinacion 

    if tiene_simbolos:
        combinacion += string.punctuation

    #Si el usuario quiere masyusculas, entoces añade mayusculas en las combinacion 
    if tiene_mayusculas:
        combinacion += string.ascii_uppercase

    #Obtiene la longitud de la combinacion de caracteres
    longitud_combinacion = len(combinacion)

    #Crear una variable para guardar el password generado
    nuevo_password = ''

    #Agrega a nuevo_password un nuevo caracter random en cada interacion 
    for _ in range(longitud):
        nuevo_password += combinacion[secrets.randbelow(longitud_combinacion)]

    return nuevo_password

if __name__ == '__main__':
    # Genera 5 passwords aleatoriamente
    for i in range(1, 6):
        nuevo_pass = generar_password(longitud=15, tiene_simbolos=True, tiene_mayusculas=True)

        especificaciones = (f'Mayusculas: {contiene_mayusculas(nuevo_pass)}, ' f'Simbolos: {contiene_simbolos(nuevo_pass)}')

        print(f'{i} -> {nuevo_pass} ({especificaciones})')