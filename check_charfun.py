import unittest
from charfun import esPalindromo
debug = 0
palindromos=["AA","Anita lava la tina","A man a plan a canal Panama","A ti no, bonita","Allí si María avisa y así va a ir a mi silla."," B B, BB"," A A","1 Ana 1","1 Ana, ANA ,,1","$1,uNU 1  $","ABBBA"]
nopalindromos=[" A"," A,","A","ABBHBA","Yo aprendro phyton","Prueba"]
class test(unittest.TestCase):

    def test_palindromo(self):
        sizeoflist = (len(palindromos))
        print("Se procesaran " + str(sizeoflist) + " Palindromos")
        i = 0
        while i < sizeoflist :
             #print(palindromos[i])
            self.assertEqual(esPalindromo(palindromos[i]),True, "El texto introducino es: \"" + palindromos[i] + "\" Se esperaba un palindromo",)
            #DEBUG
            if debug == 1 :
                print("i = " + str(i) + " palabra = " + palindromos[i])
            #FIN DEBUG
            i += 1

    def test_no_palindromo(self):
        sizeoflist = (len(nopalindromos))
        print("Se procesaran " + str(sizeoflist) + " No Palindromos")
        i = 0
        while i < sizeoflist :
            #print(nopalindromos[i])
            self.assertEqual(esPalindromo(nopalindromos[i]),False,"El texto introducino es: \"" + nopalindromos[i] + "\" No se esperaba un palindromo",)
            #DEBUG
            if debug == 1:
                print("i = " + str(i) + " palabra = " + nopalindromos[i])
            #FIN DEBUG
            i = i + 1

unittest.main()  
