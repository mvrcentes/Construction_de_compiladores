# Laboratorio No. 2 

[PDF]()

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

### 3.	Expresiones complejas 
| Epresión | Esperado |
| ---- | ---- | 
| 5 + 3 * 2 | 11 |
| 10 - 5 / 5 | 9 | 
| 100 / 25 * 2 | 8 | 

### 4.	Incluir la asignación de variables con expresiones aritméticas 
| Epresión | Esperado |
| ---- | ---- | 
| a = 5 + 3 * 2 | 11 |
| b = 10 - 5 / 5 | 9 | 
| c = 100 / 25 * 2 | 8 | 

### 5.	Manejo de errores léxicos 


### 6.	Programa con paréntesis y cambio de precedencia en operadores 
| Epresión | Esperado
| ---- | ---- | 
| 2 + 2 * 10 | 22 | 
| (2 + 2) * 10 | 40
| 2 + 2 / 2 | 3 | 
| (2 + 2) / 2 | 2 |

### 7.	Programa con comentarios de una sola línea 
| Epresión | Esperado
| ---- | ---- | 
| 2 + 2 * 10 // Operacion 1 | 22 | 
| (2 + 2) * 10 // Operacion 2 | 40
| 2 + 2 / 2 // Operacion 3 | 3 | 
| (2 + 2) / 2 // Operacion 4 | 2 |

### 8.	Programa con operadores de comparación 
| Epresión |
| ---- | 
| 1 == 1 | 
| 2 != 1 | 
| 2 < 1 |
| 2 > 1 | 
| 2 <= 5 | 
| 5 >= 5 | 

### 9.	Programa experimentando con operadores de comparación 
| Epresión | Esperado | 
| ---- | ---- |
| 1 == 1 | True |
| 2 != 1 | False | 
| 2 < 1 | False | 
| 2 > 1 | True | 
| 2 <= 5 | True | 
| 5 >= 5 | True | 


