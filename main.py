from cities import Cities
ciudades= Cities()

menu='''\n****************************
*       MENU PAISES        *
****************************
*                          *
*  i) Insertar País        *
*  e) Eliminar País        *
*  m) Modificar País       *
*  p) Imprimir Paises      *
*  x) Salir                *
*                          *
****************************'''

def main ():
   opcion= 0
   while opcion != 'X':
       print (menu)
       opcion= input("Que deseas hacer?").upper()
       
       if  opcion == 'I':
           print("******* Insertar Paises******")
           ISO3 = input("Introduce la clave ISO3 del nuevo País:  ")
           CountryName = input("Introduce el nombre del nuevo País:  ")
           Capital = input("Introduce la capital  del nuevo País:  ")
           CurrencyCode = input("Introduce el código de su moneda:  ")
           r=ciudades.inserta_ciudad(ISO3, CountryName, Capital, CurrencyCode)
           if (r== 0):
               print("-> No se pudo insertar el País...")
           else:
               print("-> El país se insertó  correctamente") 


           
       elif opcion =='E':
           print("******* Eliminar  Paises******")
           Id=int(input("Introduce el Id del país que deseas eliminar: "))
           r=ciudades.elimina_ciudad(Id)
           if (r== 0):
               print("-> El país no existe")
           else:
               print("-> El país se elimino correctamente") 



       elif opcion =='M':
           print("******* Modificar Paises******")
           Id=int(input("Introduce el Id del país que deseas Modificar: "))
           r=ciudades.buscar_pais(Id)
           if r== None:
               
               print("-> El país no existe")
           else:
               print("******* Pais a Modificar:   ")
               print(r)
               ISO3 = input("Introduce la nueva clave ISO3 del  País:  ")
               CountryName = input("Introduce el nuevo nombre del  País:  ")
               Capital = input("Introduce la nueva capital  del  País:  ")
               CurrencyCode = input("Introduce el nuevo código de su moneda:  ")
               ciudades.modifica_ciudad(Id, ISO3, CountryName, Capital, CurrencyCode)



       elif opcion =='P':
           print("******* Imprimir Paises******")
           print(ciudades)
       elif opcion =='X':
           print("-> Saliendo del Sistema")           
       else:
           print("-> Opción no válida")    






       


#pass

if __name__ == "__main__":
    main()