# EVA02_Tomas_Obreque
🧭 Descripción del proyecto

Este proyecto corresponde a la Evaluación 2 del módulo de Desarrollo de Software, en la cual se implementa un programa en Python que utiliza la API de GraphHopper para realizar geolocalización y obtener rutas entre dos puntos.
El programa solicita al usuario un medio de transporte (auto, bicicleta o caminando), las direcciones de origen y destino, y luego muestra la distancia total, la duración del viaje y las instrucciones paso a paso en español.

⚙️ Requerimientos principales

-Traducir toda la interacción con el usuario al español.

-Mostrar los valores numéricos con un máximo de dos decimales.

-Permitir salir del programa ingresando “s” o “salir”.

-Imprimir la narrativa del viaje (instrucciones paso a paso).

-Utilizar la API de GraphHopper para geocodificación y rutas.

🐍 Instrucciones de ejecución

1. Clona el repositorio:

    - git clone https://github.com/Calzetaa/EVA02_TOMAS_OBREQUE.git
    - cd EVA02_TOMAS_OBREQUE
      
2. Instala las dependencias necesarias:
   
    - pip install requests

3. Ejecuta el programa:
   
    - python3 eva02_Obreque_graphhopper_ESP.py

4. Sigue las instrucciones en pantalla:

Elige un tipo de vehículo: auto, bicicleta, o caminando.

Ingresa las direcciones de origen y destino.

Para salir, escribe s o salir.

🧩 Ejemplo de salida
===============================================
 Perfiles de vehículo disponibles:
 - auto, bicicleta, caminando
 (escriba 's' o 'salir' para terminar)
===============================================
Ingrese el perfil de vehículo que utilizará: auto
Dirección de origen: Temuco, Chile
Dirección de destino: Padre Las Casas, Chile

Distancia total: 5.23 km / 3.25 millas
Duración (hh:mm:ss): 00:08:47
Duración (horas): 0.15 h
-------------------------------------------------
Narrativa del viaje (paso a paso):
- Salga desde Temuco hacia el sur (0.50 km / 0.31 mi)
- Cruce el puente hacia Padre Las Casas (3.10 km / 1.93 mi)
- Gire a la derecha en Avenida Maquehue (1.63 km / 1.01 mi)
=================================================

