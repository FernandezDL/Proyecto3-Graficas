# Proyecto3 - OpenGL

## Contenido 
- [Descripción]()
- [Objetivo]()
- [Inputs]()
  - [Movimiento de cámara]()
    - [Con el teclado]()
    - [Con el mouse]()
  - [Cambio de shaders]()
  - [Cambio de música de fondo]()
 
## Descripción 
Siendo una especificación estándar multilenguaje y multiplataforma que se utiliza para producir gráficos en 2D y 3D, OpenGL es utilizada como la base para este tercer y último proyecto del curso. Este proyecto tiene como finalildad generar un Renderer el cual sea interactivo y en el que se puedan cargar y visualizar modelos 3D en base al Renderer trabajado durante las sesiones de clase.

## Objetivo 
El principal objetivo del proyecto es denostrar la mayor cantidad de conocimientos, si no es que todos, que se han adquirido durante todas las sesiones del semestre.

## Inputs
Al estar utilizando PyGame, la pantalla en la que se renderiza el resultado es interactiva a tiempo real, por lo que se definieron algunos inputs mediante los cuales se controla el resultado.

### Cambio de modelos
Este programa está predefinido con 4 modelos 3D entre los cuales se puede ir cambiando
- T: Dibuja, en la pantalla, el modelo 3D de una tortuga, con la textura de una tortuga realista.
- Y: Dibuja el modelo 3D de un carro, específicamente de un Porsche 911 GT2, con la textura inicial de estar hecho de metal puro.
- U: Dibuja el modelo 3D de una máquina de coser antigua, la cual tiene una textura inicial de estar tallada en madera.
- I: Dibuja el modelo 3D de un cocodrilo, el cual tiene una textura inicial de cuero

### Movimientos de cámara
_Con el teclado_
- D: Inicia la rotación del objeto sobre el eje Y, hacia la derecha.
- A: Inicia la rotación del objeto sobre el eje Y, hacia la izquierda.
- W: Mueve el modelo verticalmente hacia arriba, tiene un límite de lo que puede subir, lo cual evita que el modelo se salga de la pantalla.
- S: Mueve el modelo verticalmente hacia abajo, tiene un límite de lo que puede bajar, lo cual evita que el modelo se salga de la pantalla.
- E: Realiza un movimiento de _Zoom In_ sobre el modelo, tiene un límite de lo que se puede acercar, lo cual evita que el modelo no se vea.
- Q: Realiza un movimiento de _Zoom Out sobre el modelo, tiene un límite de lo que se puede alejar, lo cual evita que el modelo no se vea.

  
_Con el mouse_
- Moviendo el cursor hacia arriba: Si se posiciona el cursor en la pantalla emergente y se sube, el modelo procederá a moverse verticalmente hacia arriba. También cuenta con el límite de lo que puede subir, para evitar que el modelo se salga de la pantalla.
- Moviendo el cursor hacia abajo: Si se posiciona el cursor en la pantalla emergente y se baja, el modelo procederá a moverse verticalmente hacia abajo. También cuenta con el límite de lo que puede bajar, para evitar que el modelo se salga de la pantalla.
- Moviendo el _scroll_ hacia arriba: Si se realiza un movimiento del _scroll_ hacia arriba, el modelo procederá a hacer un _Zoom In_. También se cuenta con el límite de lo que puede acercar, para evitar que el modelo no se vea.
- Moviendo el _scroll_ hacia abajo: Si se realiza un movimiento del _scroll_ hacia abajo, el modelo procederá a hacer un _Zoom Out_. También se cuenta con el límite de lo que puede alejar, para evitar que el modelo no se vea.

### Cambio de Shaders
_Con el teclado_
- 1 - Versión original

  Es la versión original del modelo, con la textura que se define en el programa principal y con su forma normal
- 2 - Pie_shader

  Este shader simula ser un Pie de cereza, teniendo sus secciones coloreadas simulando la masa y el relleno
- 3 - Siren_shader

  Este genera un cambio en el color del modelo, haciendo un efecto de transición entre tonos de verde y azul
- 4 - glitch_shader

  Con el glitch_shader se genera un efecto de _falla_, en el cual el modelo se muestra por algunos segundos y desaparece por otro poco de tiempo
- 5 - mixColors_shader

  Habiendo definido dos colores, este shader interpola los colores según la coordanada y del pixel correspondiente

### Cambio de música de fondo
Cuando comienza a correr el programa automáticamente se comenzará a reproducir una canción, en este caso se reproducirá _« Niñas de Instagram - Joaquina »_, sin embargo esta canción se puede ir cambiando entre cuatro posibles opciones.

- Z: Reproduce la canción _« Niñas de Instagram - Joaquina »_ desde el inicio.
- X: Reproduce la canción _« Ni me debes ni te debo - Carin león ft. Camilo »_ desde el inicio.
- C: Reproduce la canción _« Conteo regresivo - Gilberto Santa Rosa »_ desde el inicio.
- V: Reproduce la canción _« Adiós, Adiós - TIMØ »_ desde el inicio.
