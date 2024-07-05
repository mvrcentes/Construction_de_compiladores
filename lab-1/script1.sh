#!/bin/sh

# Nombre de la imagen de Docker
IMAGE_NAME="compiler_env"

# Directorio que contiene el Dockerfile y los archivos fuente
BUILD_CONTEXT=$(pwd)

# Archivo temporal para almacenar las expresiones
INPUT_FILE="input.txt"

# Mensaje de estado
echo "Construyendo la imagen Docker..."

# Construye la imagen Docker
docker build -t $IMAGE_NAME $BUILD_CONTEXT

# Verifica si la construcción fue exitosa
if [ $? -ne 0 ]; then
  echo "Error: La construcción de la imagen Docker falló."
  exit 1
fi

# Mensaje de estado
echo "La imagen Docker ha sido construida con éxito."

# Hardcodear las expresiones
cat << EOF > $INPUT_FILE
a = 5
b = 10
c = a + b
EOF

# Mensaje de estado
echo "Ejecutando el contenedor Docker..."

# Ejecuta el contenedor Docker, montando el archivo temporal en /usr/src/app/input.txt dentro del contenedor
docker run --rm -it -v $(pwd)/$INPUT_FILE:/usr/src/app/input.txt $IMAGE_NAME

# Limpia el archivo temporal después de la ejecución
rm $INPUT_FILE

# Mensaje de estado
echo "Ejecución completada."
