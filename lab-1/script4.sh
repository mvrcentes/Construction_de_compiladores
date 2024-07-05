#!/bin/sh

# Nombre de la imagen de Docker
IMAGE_NAME="compiler_env"

# Directorio que contiene el Dockerfile y los archivos fuente
BUILD_CONTEXT=$(pwd)

# Archivo temporal para almacenar las expresiones
INPUT_FILE="input.txt"

# Construye la imagen Docker
echo "Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME $BUILD_CONTEXT

# Verifica si la construcción fue exitosa
if [ $? -ne 0 ]; then
  echo "Error: La construcción de la imagen Docker falló."
  exit 1
fi
echo "La imagen Docker ha sido construida con éxito."

# Hardcodear las expresiones
cat << EOF > $INPUT_FILE
a = 5
b = 10
c = a + b / 2  
d = 1 + c * 2  
e = b / 2 + 5 * d - 3 
EOF

# Ejecuta el contenedor Docker, montando el archivo temporal en /usr/src/app/input.txt dentro del contenedor
echo "Ejecutando el contenedor Docker..."
docker run --rm -it -v $(pwd)/$INPUT_FILE:/usr/src/app/input.txt $IMAGE_NAME

# Limpia el archivo temporal después de la ejecución
rm $INPUT_FILE

echo "Ejecución completada."

# Referencias
# Devpool. (18 de 1 de 2019). stackoverflow. Obtenido de Running a script inside a docker container using shell script: https://stackoverflow.com/questions/31578446/running-a-script-inside-a-docker-container-using-shell-script
# Docker. (n/a). Docker Community Forums . Obtenido de Executing the Shell Script through Dockerfile: https://forums.docker.com/t/executing-the-shell-script-through-dockerfile/134152/1
# ChatGPT 
# COPILOT 
