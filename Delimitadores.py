class Pelicula:
    DELIMITER = "|"
    
    def __init__(self, id_pelicula, titulo, genero, duracion):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
    
    def to_string(self):
        return f"{self.id_pelicula}{self.DELIMITER}{self.titulo}{self.DELIMITER}{self.genero}{self.DELIMITER}{self.duracion}\n"
    
    @staticmethod
    def from_string(line):
        data = line.strip().split(Pelicula.DELIMITER)
        if len(data) == 4:
            return Pelicula(data[0], data[1], data[2], data[3])
        return None

def agregar_pelicula(archivo, pelicula):
    with open(archivo, "a") as f:
        f.write(pelicula.to_string())

def imprimir_peliculas(archivo):
    try:
        with open(archivo, "r") as f:
            for line in f:
                pelicula = Pelicula.from_string(line)
                if pelicula:
                    print(f"ID: {pelicula.id_pelicula}, Título: {pelicula.titulo}, Genero: {pelicula.genero}, Duracion: {pelicula.duracion} min")
    except FileNotFoundError:
        print("El archivo no existe.")

def buscar_pelicula(archivo, id_pelicula):
    try:
        with open(archivo, "r") as f:
            for line in f:
                pelicula = Pelicula.from_string(line)
                if pelicula and pelicula.id_pelicula == id_pelicula:
                    return pelicula
    except FileNotFoundError:
        print("El archivo no existe.")
    return None

def modificar_pelicula(archivo, id_pelicula, nuevo_titulo, nuevo_genero, nueva_duracion):
    peliculas = []
    try:
        with open(archivo, "r") as f:
            for line in f:
                pelicula = Pelicula.from_string(line)
                if pelicula and pelicula.id_pelicula == id_pelicula:
                    pelicula.titulo = nuevo_titulo
                    pelicula.genero = nuevo_genero
                    pelicula.duracion = nueva_duracion
                peliculas.append(pelicula)
        with open(archivo, "w") as f:
            for pelicula in peliculas:
                f.write(pelicula.to_string())
    except FileNotFoundError:
        print("El archivo no existe.")

def eliminar_pelicula(archivo, id_pelicula):
    peliculas = []
    try:
        with open(archivo, "r") as f:
            for line in f:
                pelicula = Pelicula.from_string(line)
                if pelicula and pelicula.id_pelicula != id_pelicula:
                    peliculas.append(pelicula)
        with open(archivo, "w") as f:
            for pelicula in peliculas:
                f.write(pelicula.to_string())
    except FileNotFoundError:
        print("El archivo no existe.")

# Ejemplo de uso
archivo_peliculas = "peliculas.txt"
agregar_pelicula(archivo_peliculas, Pelicula("1", "Inception", "Ciencia Ficcion", "148"))
agregar_pelicula(archivo_peliculas, Pelicula("2", "Titanic", "Romance", "195"))
imprimir_peliculas(archivo_peliculas)
modificar_pelicula(archivo_peliculas, "1", "Origen", "Sci-Fi", "150")
eliminar_pelicula(archivo_peliculas, "2")
imprimir_peliculas(archivo_peliculas)