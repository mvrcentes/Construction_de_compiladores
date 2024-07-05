# Laboratorio No. 1

[PDF](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-1/lab-1/Laboratorio_No1.pdf)

## Requisitos
1. Terminal con Bash, Sh, Zsh, Fish
2. Docker 

## Entregables

Para que funcionen los scriprs estar dentro de la carpte de `lab-1`

### 1. Crear un programa de asignación 

#### Valores probados port el script 
| Expresiones |
| ---- |
| a = 5 |
| b = 10 | 
| c = a + b |

#### Correr el programa

1. Darle permisos al script con el siguiente comando
```bash
chmod +x script1.sh
```
2. Correr el script 
```bash
./script1.sh
```

![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-1/lab-1/images/entregable-1.png?raw=true)

### 2. Crear un programa de operación

#### Valores probados por el script 
| Expresión | Valor esperado |
| ---- | ---- |
| a = 10 | n/a |
| b = 20 | n/a |
| c = a + b | 30 |
| d = c * 2 | 60 |
| e = d - 5 | 55 |
| f = e / 3 | 18 |

#### Correr el programa

1. Darle permisos al script con el siguiente comando
```bash
chmod +x script2.sh
```
2. Correr el script 
```bash
./script2.sh
```
![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-1/lab-1/images/entregable-2.png?raw=true)

### 3. Agregar manejo de errores

#### Valores probados por el script 
| Expresión | 
| ---- | 
| a = ) |
| b = $ | 

#### Correr el programa

1. Darle permisos al script con el siguiente comando
```bash
chmod +x script3.sh
```
2. Correr el script 
```bash
./script3.sh
```

![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-1/lab-1/images/entregable-3.png?raw=true)

### 4. Experimentar con la precedencia

#### Valores probados por el script 
| Expresión | Valor esperado |
| ---- | ---- |
| a = 5 | n/a | 
| b = 10 | n/a | 
| c = a + b / 2 | 10 | 
| d = 1 + c * 2 | 21 | 
| e = b / 2 + 5 * d - 3 | 107 | 

#### Correr el programa

1. Darle permisos al script con el siguiente comando
```bash
chmod +x script4.sh
```
2. Correr el script 
```bash
./script3.sh
```

![](https://github.com/mvrcentes/Construction_de_compiladores/blob/Lab-1/lab-1/images/entregable-4.png?raw=true)

## Rubrica 
| Puntos | Requisito | Check | Comentario |
|----|----|----|----|
10 | Crear un programa de asignaciónn | ✅ | 
15 | Crear un programa de operación | ✅ | 
15 | Agregar manejo de errores | ✅ | 
15 | Experimentar con la precedencia | ✅ | 
10 | Completar todas las tareas | ✅ | todos los programas están
10 | Respuestas comprensibles y claras | ✅ | presentación bien estructurada
10 | Seguimiento de instrucciones | ✅ | paso a paso | 
10 | Organización y presentación adecuada | ✅ | apoco no se ve bonito | 
