## Biblioteca-grafos 

Este repositorio contiene una biblioteca orientada a objetos en Python 3 para la generación y visualización de grafos, así como la implementación de distintos modelos clásicos de generación de grafos aleatorios.

El proyecto fue desarrollado como parte del curso Diseño de Algoritmos. 

# Modelos implementados

Se implementan los siguientes modelos de generación de grafos:

       >> Modelo de Malla 

       >> Modelo de Erdős–Rényi 

       >> Modelo de Gilbert 

       >> Modelo Geográfico Simple 

       >> Modelo de Dorogovtsev–Mendes

       >> Modelo de Barabási–Albert

Cada modelo genera grafos dirigidos o no dirigidos, según el parámetro correspondiente. 

# Estructura del proyecto 

Biblioteca-grafos/
│
├── src/
│   ├── grafo.py          # Clases Nodo, Arista y Grafo
│   └── modelos.py        # Implementación de los modelos
│
├── tests/                # Scripts de prueba
│
├── outputs/
│   ├── gv/               # Archivos GraphViz (.gv)
│   └── img/              # Imágenes generadas con Gephi
│
├── generate_all_gv.py    # Script para generar todos los grafos
└── README.md

# Uso  

Desde la raíz del proyecto, ejecutar:

    python generate_all_gv.py


Este script genera automáticamente:

    >> 18 archivos .gv (3 tamaños por cada modelo)

    >> Tamaños: 50, 200 y 500 nodos

    >> Los archivos se guardan en outputs/gv/ 

# Visualizacion  

Los archivos .gv pueden abrirse directamente en Gephi:

    1. Abrir Gephi

    2. File → Open

    3. Seleccionar el archivo .gv

    4. Aplicar el layout ForceAtlas2

    5. Exportar la imagen (.png o .svg) a outputs/img/ 


# Resultados

Las imágenes finales de los grafos generados se encuentran en:

    outputs/img/


Cada imagen corresponde a un archivo .gv generado por el script. 

# Autor

Daniel Vázquez
Instituto Politécnico Nacional
Maestría en Ciencias de la Computación