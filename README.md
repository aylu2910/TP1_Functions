## TP1_Functions
1. Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). 
En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). 
Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el 
máximo hallado, o un mensaje informativo si éste no existe.

2. Desarrollar una función que reciba tres números enteros positivos y verifique si 
corresponden a una fecha válida (día, mes, año). Devolver True o False según la 
fecha sea correcta o no. Realizar también un programa para verificar el comporta￾miento de la función.

3. Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro￾llar una función que reciba como parámetro la cantidad de viajes realizados en un 
determinado mes y devuelva el total gastado en viajes. Realizar también un pro￾grama para verificar el comportamiento de la función.

    ![image](https://user-images.githubusercontent.com/36941575/116017559-532ecf00-a616-11eb-8cd8-9a07c235a8ca.png)

4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
dos números enteros, correspondientes al total de la compra y al dinero recibido. 
Informar cuántos billetes de cada denominación deben ser entregados al cliente 
como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que 
existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error 
si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abo￾na con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete 
de $20, 1 billete de $10 y 3 billetes de $1.

5. Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones 
de asteriscos, donde la cantidad de filas se recibe como parámetro:

![image](https://user-images.githubusercontent.com/36941575/116017771-eb2cb880-a616-11eb-838d-7a7aef4a222e.png)

6. Desarrollar una función que reciba como parámetros dos números enteros positi￾vos y devuelva el número que resulte de concatenar ambos valores.
Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase.


7. Escribir una función diasiguiente(…) que reciba como parámetro una fecha cual￾quiera expresada por tres enteros (correspondientes al día, mes y año) y calcule y 
devuelva tres enteros correspondientes el día siguiente al dado.
Utilizando esta función, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

8. La siguiente función permite averiguar el día de la semana para una fecha determi￾nada. La fecha se suministra en forma de tres parámetros enteros y la función de￾vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para imprimir por pantalla el calendario de un mes completo, correspondiente a un 
mes y año cualquiera basándose en la función suministrada. Considerar que la semana comienza en domingo.
![image](https://user-images.githubusercontent.com/36941575/116017675-a7d24a00-a616-11eb-93ae-68a2b0d5403f.png)

9. Resolver el siguiente problema diseñando y utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el pe￾so para poder cargar el camión de reparto. La empresa cuenta con N camiones, y 
cada uno puede transportar hasta media tonelada (500 kilogramos).
En un cajón caben 100 naranjas con un peso entre 200 y 300 gramos cada una. Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar 
como jugo.
Se solicita desarrollar un programa para ingresar la cantidad de naran￾jas cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son 
para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto. Simular el peso de cada unidad generando un número entero al 
azar entre 150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del camión no debe ser inferior al 80%; en 
caso contrario el camión no serán despachado por su alto costo. 
