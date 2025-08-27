class F:

    def read(filename):
        with open(filename, 'r', encoding="utf-8") as file:
            
            for linea in file:
                print(linea.strip())
    
    def write_diciotnary(self, filename, dictionary):
        enable = 1
        id = 1
        
        # Abrimos el archivo con la opción de escritura:
        with open(filename, 'w', encoding="utf-8") as file:

            # Extraemos las columnas del archivo del diccionario:
            labels = list(dictionary[0].keys())
            file.write("id,")

            # Escribimos las columnas del diccionario en el archivo:
            for label in labels:
                file.write(label + ",")
            file.write("status" + "\n")

            # Llenamos el archivo en sus respectivas columnas con la información del diccionario:
            for key in diccionario:
                count = 0
                
                # Escribimos el ID:
                file.write(str(id) + ",")

                for value in key.values():

                    # Escribimos el valor
                    file.write(d)
                    count += 1
                    file.write(",")
                
                id += 1
                file.write(str(enable) + "\n")
    
    def write_array(self, filename, list):
        with open(filename, 'w', encoding="utf-8") as file:

            # Recorremos la matriz y accedemos a las listas o filas dentro de la matriz:
            for values in list:
                data = values.split(",")
                c = 0

                # Recorremos las listas o filas de la matriz:
                for d in data:
                    file.write(f"{d}")
                    
                    if c <= len(data) - 1:
                        file.write(",")
                    
                    file.write("\n")



    # Función de eliminación:
    def delete(self, filename, id):
        list = []

        with open(filename, 'r', encoding='utf-8') as file:
            
            # Accedemos a las filas o registros del archivo:
            list = file.readlines()

        newlist = []
        # Recorremos las filas o registros:
        for l in list:
            arr = l.strip().split(',')

            # Accedemos y p´reguntamos por el valor de la columna 'id':
            if str(arr[0]) == str(id):
                print(id)
                arr[len(arr) - 1] = "0"
                ll = ""
                count = 1

                for a in arr:
                    ll = ll + str(a)
                    if count < len(arr):
                        ll = ll + ","
                    count += 1
                
                l = ll + "\n"

            newlist.append(l)
            




f = F()
f.read("notes.txt")

