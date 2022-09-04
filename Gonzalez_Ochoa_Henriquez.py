#Laboratorio 1 seguirdad informática
#Diego González
#José Ochoa
#Ignacio Henríquez
import requests
abc = "abcdefghijklmnopqrstuvwxyz"
abc2 = "abcdefghijklmnopqrstuvwxyz"

def main():
    seguir = True
    while(seguir):
        print("Desafio 1 = 1")
        print("Desafio 2 = 2")
        print("Para salir presione cualquier caracter")
        opcion = int(input("Indique que el numero del desafio que quiere mostrar: "))
        print(" ")
        if(opcion == 1):
            clave = "heropassword"
            c = input("codigo a cifrar: ").lower()
            rot8 = rot(c,8)
            vig = vigerente(rot8,clave)
            cifrado = rot(vig,12)
            print(cifrado)
            rot21 = rot(cifrado,-12)
            desvig = desvigerente(rot21,clave)
            desifrado = rot(desvig,-8)
            print(desifrado)
            headers = {
                'Content-Type': 'text/plain',
            }

            data = '{"msg":"'+cifrado+'"}'

            response = requests.post('https://finis.mmae.cl/SendMsg', headers=headers, data=data)
    
        elif(opcion == 2):
            
    
            clave = "finispasswd"
            headers = {
                'Content-Type': 'text/plain',
            }
            response = requests.get('https://finis.mmae.cl/GetMsg', headers=headers)
            mensaje = response.json()
            print(mensaje['msg'])
            descifrar = mensaje['msg'].lower()
            rot21 = rot(descifrar,-12)
            desvig = desvigerente(rot21,clave)
            desifrado = rot(desvig,-8)
            print(desifrado)

        else:
            print("Adios")
            seguir = False

def rot(cadena,clave):
    text_cifrado = ''
    for letra in cadena:
        suma = abc.find(letra) + clave
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])
        
    return text_cifrado
    

def vigerente(cadena,clave):
    text_cifrar = ""

    i = 0
    for letra in cadena:
        suma = abc2.find(letra) + abc2.find(clave[i % len(clave)])
        modulo = int(suma) % len(abc)
        text_cifrar = text_cifrar + str(abc2[modulo])
        i = i+1
    return text_cifrar

def desvigerente(cadena,clave):
    text_cifrar = ""

    i = 0
    for letra in cadena:
        suma = abc.find(letra) - abc.find(clave[i % len(clave)])
        modulo = int(suma) % len(abc)
        text_cifrar = text_cifrar + str(abc[modulo])
        i = i+1
    return text_cifrar

main()







