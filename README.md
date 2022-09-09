# Reto_Inicial
El link del repositorio es el siguiente: [Github:https://github.com/paulaanb/Reto_Inicial]

Este trabajo en grupo esta compuesto por los siguientes integrantes:
- Paula Naranjo
- Carmen Martín
- Andrea Manuel
- Ana López
- Laura Rodríguez

La descripción del reto es el siguiente:

Para comenzar a introducir al alumno en esta mecánica práctica se puede plantear un primer ejercicio: “Resuelva el problema de mover el caballo de ajedrez sobre el teclado de un teléfono”.
Suponga que tiene a su disposición dicha ficha del ajedrez, y que se puede mover en ciertas formas particulares como se observa en la figura 1. Ahora, desea saber cuántos movimientos válidos pueden realizarse partiendo con el caballo desde todos los números del teclado realizando un movimiento desde cada número.

Si se parte del 1 se puede ir al 6 y al 8 (dos movimientos); si se sale del 2 se puede llegar al 7 y al 9 (dos movimientos más); iniciando desde el 3 se puede arribar al 4 y al 8 (se suman nuevamente dos); si se arranca desde el 4 las posibilidades son 3, 9 y 0 (ahora se acumulan tres movimientos); pero si la posición inicial es el 5 no se puede mover la ficha a ningún lugar dado que no hay movimientos válidos - sin embargo aún restan varias posibilidades más para seguir probando–; desde el 6 se pueden alcanzar el 1, 7 y 0 (nuevamente se agregan tres más); por su parte desde el 7 se puede mover la ficha hasta el 2 y el 6 (la cantidad se incrementa en dos); si se toma el 8 como inicio se pueden alcanzar el 1 y el 3 (se adicionan dos movimientos); si se posiciona la ficha en el 9 las opciones para moverse son 2 y 4 (nuevamente se tienen dos movimientos); y por último si se sale desde el 0 los movimientos válidos son 4 y 6 (se suman los últimos dos). En total se pueden realizar veinte movimientos válidos con esta ficha.
 
Ahora, diseñe un algoritmo que permita calcular cuántos posibles movimientos válidos puede realizar la ficha del caballo, recibiendo como entrada la cantidad de movimientos a realizar desde el inicio, partiendo de todos los números. Por ejemplo, como mostramos anteriormente si la cantidad de movimientos es uno, la cantidad de movimientos válidos son veinte. Pero si la cantidad de mo- vimientos son dos y se sale desde el 1 se puede ir hasta el 6 y el 8 (un movimiento), a continuación, a partir del 6 hasta el 1, 7 y 0 (dos movimientos de la ficha), luego se sigue desde el 8 hasta el 1 y 3 (para alcanzar los dos movimientos de la ficha). En resumen, se tienen cinco posibles movimientos válidos partiendo desde el 1 (1-6-1, 1-6-7, 1-6-0, 1-8-1 y 1-8-3) a estos se deben sumar todos los movimientos que resulten de partir de los demás número. En total la cantidad de posibles movimientos válidos para dos movimientos son 46. Una vez desarrollado el algoritmo complete la siguiente tabla.

| Cantidad de movimientos | Posibilidades válidas |
| ------------- | ------------- |
| 1 | 20 |
| 2 | 46 |
| 3 | 104 |
| 5	|   |
| 8 |   |	
| 10 |   |	
| 15	|   |
| 18	|   |
| 21 |   |	
| 23 |   |	
| 32 |   |

Pasemos a trabajar en otro ejemplo para fortalecer aún más nuestro pensamiento algorítmico, en este caso el problema de las n-reinas, el mismo consiste en ubicar n reinas en un tablero de ajedrez de tamaño n x n, sin que las mismas se amenacen. Recuerde que la reina desplaza de manera horizontal, vertical y diagonal. Nótese que una parte importante para resolver un problema es de que manera representar la solución, para este caso particular usamos un vector de n posiciones (columnas) y el valor almacenado representa la fila donde se ubica dicha reina.

Cuando haya entendido el problema y tenga una solución en mente, desarrolle un algoritmo que permita hallar al menos una solución para distintas cantidades de reinas, y luego complete la siguiente tabla.

| n-reinas |	Soluciones distintas	| Todas las soluciones	| Una solución |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 1 | 1 | [0] |
| 2	| 0 | 0 | - |
| 3	| 0 | 0 | - |
| 4	| 1	| 2	| [1, 4, 0, 3] |
| 5 | 2 | 10 |   |	
| 6 | 1	| 4	|   |
| 7	| 6 | 40	|   |
| 8	| 12	| 92	|   |
| 9	| 46 | 352	|   |
| 10	| 92	| 724	|  |
| 15	| 285.053	| 2.279.184	|   |
