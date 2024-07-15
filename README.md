# Laboratorio No. 2 

[PDF](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Laboratorio_No2.pdf)

## Entregables 

```Para poder correr todos los programas se necesita estar dentro del docker, para eso corremos el siguiente programa ```

```bash
docker run --rm -ti -v "$(pwd)/program:/program" lab2-image
```

### 1. Programa que asigne un valor a una variable 

| Epresión |
| ---- | 
| a = 5 | 
| b = 10 | 
| c = 178 |

#### Correr el programa
```bash 
python3 Driver.py program_1.txt
```
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-1.png)

### 2. Crear un programa con una operación simple

| Epresión | Esperado | 
| ---- | ---- | 
| 5 + 10 | 15 |
| 7 + 3 | 10 |
| 53 + 9 | 62 | 

#### Correr el programa
```bash 
python3 Driver.py program_1.txt
```

![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-2.png)

### 3.	Expresiones complejas 
| Epresión | Esperado |
| ---- | ---- | 
| 5 + 3 * 2 | 11 |
| 10 - 5 / 5 | 9 | 
| 100 / 25 * 2 | 8 | 

![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-3.png)

#### Correr el programa
```bash 
python3 Driver.py program_3.txt
```

### 4.	Incluir la asignación de variables con expresiones aritméticas 
| Epresión | Esperado |
| ---- | ---- | 
| a = 5 + 3 * 2 | 11 |
| b = 10 - 5 / 5 | 9 | 
| c = 100 / 25 * 2 | 8 | 

#### Correr el programa
```bash 
python3 Driver.py program_4.txt
```
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-4.png)

### 5.	Manejo de errores léxicos 
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-5.png)

### 6.	Programa con paréntesis y cambio de precedencia en operadores 
| Epresión | Esperado
| ---- | ---- | 
| 2 + 2 * 10 | 22 | 
| (2 + 2) * 10 | 40
| 2 + 2 / 2 | 3 | 
| (2 + 2) / 2 | 2 |

![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-6.png)

#### Correr el programa
```bash 
python3 Driver.py program_6.txt
```

### 7.	Programa con comentarios de una sola línea 
| Epresión | Esperado
| ---- | ---- | 
| 2 + 2 * 10 // Operacion 1 | 22 | 
| (2 + 2) * 10 // Operacion 2 | 40
| 2 + 2 / 2 // Operacion 3 | 3 | 
| (2 + 2) / 2 // Operacion 4 | 2 |

#### Correr el programa
```bash 
python3 Driver.py program_7.txt
```

![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-7.png)

### 8.	Programa con operadores de comparación 
| Epresión |
| ---- | 
| 1 == 1 | 
| 2 != 1 | 
| 2 < 1 |
| 2 > 1 | 
| 2 <= 5 | 
| 5 >= 5 | 

#### Correr el programa
```bash 
python3 Driver.py program_8_9.txt
```
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-8-9.png)

### 9.	Programa experimentando con operadores de comparación 
| Epresión | Esperado | 
| ---- | ---- |
| 1 == 1 | True |
| 2 != 1 | False | 
| 2 < 1 | False | 
| 2 > 1 | True | 
| 2 <= 5 | True | 
| 5 >= 5 | True | 

#### Correr el programa
```bash 
python3 Driver.py program_8_9.txt
```
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-8-9.png)

### 10.	Estructuras de control como “if” y “while” 

#### Correr el programa
```bash 
python3 Driver.py program_10_11.txt
```
```bash 
python3 Driver.py program_10_12.txt
```

### 11.	Programa que utilice estructura “if” 

```bash
x = 1
y = 2
if (x == y) then
    x
else
    y
endif

```

#### Correr el programa
```bash 
python3 Driver.py program_10_11.txt
```
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-10-11.png)

### 12.	Programa que utilice estrcutra “while” 
```bash
a = 0
while a < 5 do
  a = a + 1
endwhile
```

#### Correr el programa
```bash 
python3 Driver.py program_10_11.txt
```
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-10-12.png)

### 13.	Soporte de funciones definidas por el usuario 
#### Correr el programa
```bash 
python3 Driver.py program_13_14.txt
```
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-14.png)

### 14.	Programa que defina y llame una función 
#### Correr el programa
```bash 
python3 Driver.py program_13_14.txt
```
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-14.png)

### 15.	Implementación de sistema de tipos
```bash
"hola"+"mundo"
2*"Hola" + 2*"Mundo"
```

#### Correr el programa
```bash 
python3 Driver.py program_15.txt
```

![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-2/lab-2/Entregables/Images/entregable-15.png)

## Rubrica 
| Puntos | Requisito | Check | Comentario |
|----|----|----|----|
5 | Crear un programa que asigne un valor a una variable (1) | ✅ | 
5 | Crear un programa que realice una operacion aritmetica simple (2) | ✅ | 
10 | Experimentar con expresiones m ́as complejas (3) | ✅ | 
10 | Modificar el lenguaje para incluir la asignacion de variables con expresiones aritm ́eticas (4) | ✅ | 
10 | Agregar manejo de errores al compilador para detectar tokens inv ́alidos (5)| ✅ | 
5 | Crear un programa que utilice par ́entesis para cambiar la precedencia (6) | ✅ | 
10 | Extender el lenguaje para soportar comentarios (7) | ✅ |  | 
10 | Agregar operadores de comparacion al lenguaje (8) | ✅ |  | 
5 | Crear un programa que utilice operadores de comparación (9) | ✅ |  | 
10 | Extender el lenguaje para soportar estructuras de control (10) | ✅ |  | 
5 | Crear un programa que utilice una estructura ‘if‘ (11) | ✅ |  | 
5 | Crear un programa que utilice una estructura ‘while‘ (12) | ✅ |  | 
10 | Agregar soporte para funciones definidas por el usuario (13) | ✅ |  | 
5 | Crear un programa que defina y llame a una funcion (14) | ✅ |  | 
10 | Implementar un sistema de tipos básico (15) | ✅ |  | 
