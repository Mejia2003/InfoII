# Sistema de Gestión de Imágenes DICOM en Python
 Bienvenido al tutorial del sistema de Gestión de Imágenes DICOM en Python, donde se abarcará la optimizanción de la gestión de datos, protegiendo la privacidad del paciente y facilitando el análisis de imágenes médicas.
 

------------


 
###### Instrucciones: 
 El tutorial consiste en una serie de pasos para realizar la gestión avanzada de imágenes DICOM, incluyendo la anonimización, organización y conversión a formato NIfTI
 

------------


 
####  Paso 0. Definición del problema.

En el ámbito de la investigación clínica, la gestión de imágenes médicas y su correspondiente metadata es fundamental para garantizar tanto la integridad del proceso investigativo como la privacidad de los pacientes. Las imágenes DICOM, que contienen datos detallados tanto clínicos como personales, requieren un manejo cuidadoso para evitar la divulgación de información identificable.



![image](https://github.com/Mejia2003/InfoII/assets/159477450/ac479e12-f04b-4059-8304-f42df2cf1361)




------------

 
#### Paso 1. Desarrollar el diagrama de clase. 

Para el desarrollo del diagrama de Clases para el Sistema de Gestión de Imágenes DICOM, nos enfocamos en 3 clases diferentes usando la programación orientada a objetos para diseñar clases que encapsulen las funcionalidades necesarias, promoviendo la reutilización del código y la fácil mantenibilidad.

-  Clase Estudio
##### Atributos:
ID de estudio

ID de paciente

Fecha de adquisición

Modalidad

Descripción

Imágenes DICOM

Información del estudio (dimensiones, etc.)
##### Métodos:
Cargar estudio DICOM

Anonimizar estudio

Convertir a formato NIfTI

Visualizar imágenes (plano único, tres planos o mosaico)

Obtener información del estudio

Todos los atributos de la clase Estudio tienen un encapsulamiento privado, para evitar la filtración de datos sensibles tanto del estudio como del paciente y los métodos tienen encapsulamiento público.

-  Clase Paciente:
##### Atributos:

ID de paciente

Nombre del paciente

Lista de estudios asociados
##### Métodos:

Agregar estudio

Consultar estudios

Eliminar estudio

Obtener información del paciente

Todos los atributos de la clase Paciente tienen un encapsulamiento privado, para evitar la filtración de datos sensibles tanto del estudio como del paciente y los métodos tienen encapsulamiento público.

- Clase SistemaGestion:
##### Atributos:
Lista de pacientes
##### Métodos:

Agregar paciente

Consultar paciente

Eliminar paciente

Buscar estudio por ID de paciente y ID de estudio

Obtener lista de pacientes

Obtener información del sistema

Todos los atributos de la clase SistemaGestion tienen un encapsulamiento privado, para evitar la filtración de datos sensibles tanto del estudio como del paciente y los métodos tienen encapsulamiento público.

Para ver el diagrama de clase completo  con sus respectivas relaciones entre las 3 diferentes clases, por favor de click sobre  Diagrama de clase


![Captura de pantalla 2024-05-19 144715](https://github.com/Mejia2003/InfoII/assets/159477450/cc0dacf1-3468-48b7-b3f1-2690a8831176)





------------



#### Paso 2. Configurar el entorno de trabajo
Prepararemos el entorno de trabajo para garantizar que todas las dependencias estén instaladas y listas para su uso.

Las librerías utilizadas son:



##### pydicom:

Librería para el manejo de archivos DICOM:
Carga y lee archivos DICOM, que son el formato estándar para almacenar imágenes médicas.
Extrae información relevante de los archivos DICOM, como datos del paciente, fecha de adquisición, modalidad de imagen, etc.
Permite manipular y procesar datos de imagen DICOM.

 ##### Numpy:

Librería para computación numérica:
Ofrece estructuras de datos eficientes para manejar arrays multidimensionales (como imágenes 3D o 4D).
Proporciona funciones para realizar operaciones matemáticas y científicas sobre arrays.
Facilita el preprocesamiento y análisis de datos numéricos, incluyendo imágenes médicas.

##### Nilearn:

Librería especializada en neuroimagen:
Ofrece herramientas para cargar, preprocesar, analizar y visualizar datos de neuroimagen.
Incluye algoritmos para el análisis de resonancia magnética funcional (fMRI), tomografía por emisión de positrones (PET), etc.
Permite realizar estudios de conectividad cerebral, mapeo de funciones cerebrales y otras tareas de neurociencia.

##### Nilearn.plotting:

Submódulo de nilearn para visualización de neuroimagen:
Proporciona funciones para mostrar imágenes cerebrales 3D o 4D.
Permite personalizar la visualización, como la orientación de la imagen, el rango de valores y la paleta de colores.
Facilita la creación de figuras y gráficos para comunicar resultados de estudios neurocientíficos.

Puedes instalar los requerimientos así:
**python -m pip install numpy**

------------

#### Paso 3. 
