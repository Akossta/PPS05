debug=0

def check_input(texto):
    if texto == "":
        print("No se ha introducido ningun texto")
        return False
    else:
        #procesar el texto y eliminar espacios, tildes, mayusculas, caracteres especiales
        texto = texto.lower()
        texto = texto.replace(" ", "")
        texto = texto.replace("á", "a")
        texto = texto.replace("é", "e")
        texto = texto.replace("í", "i")
        texto = texto.replace("ó", "o")
        texto = texto.replace("ú", "u")
        texto = texto.replace("ü", "u")
        texto = texto.replace(",", "")
        texto = texto.replace(".", "")
        texto_limpio = texto
        #DEBUG
        if debug == 1:
            print('Numero de caracteres despues de procesar ' + str(len(texto_limpio)))
        #FIN DEBUG
        if len(texto_limpio) >= 2:
            return texto_limpio
        else:
            print("El texto es demasiado corto")
            return False
        
def esPalindromo(texto):
#Verificamos si es palindromo
    texto_limpio=check_input(texto)
    if texto_limpio == False:
        return False
    if texto_limpio == texto_limpio[::-1]:
        #DEBUG
        if debug == 1:
            print("Es palindromo")
        #FIN DEBUG
        return True
    else:
        #DEBUG
        if debug == 1:
            print("No es palindromo")
        #FIN DEBUG
        return False

def main():
    texto = input("Introduce el texto: ")
    esPalindromo(texto)

if __name__ == "__main__":
    main()