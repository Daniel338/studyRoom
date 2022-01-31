Study Syntax of Markdown
========================

En el lenguaje Markdown encontraras **tres tipos de elementos basicos**(bloque, linea y varios) que a su vez  
engloban el resto de la sintaxis. considera esto una *cheat sheet* con la que guiarte.  

Elementos de bloque
-------------------

Un elemento en bloque ocupa todo el espacio de su elemento padre (contenedor),  
creando asi un "bloque".

### Parrafos y saltos de linea:  
Para generar un parrafo basta con escribir el texto. Si quieres generar un salto de linea puedes precionar dos veces intro `↩` o dejar 2 espacios en blanco al final de la linea.  

    Este es un párrafo.

    Y este es otro párrafo.

> **Nota**: Debes tener en cuenta no agregar sangrías o espacios al inicio del parrafo,  
> esto probocara un error en el formato.

Tambien puedes usar la etiqueta `<br>` al final de la linea para generar un salto de linea.

### Encabezados:  
Los encabezados se crean usando el carácter `#` delante de la oración. Los Encabezados  
pueden ser de **diferentes niveles**, con tantos `#` seguidos como el nivel del encabezado.  

    # Este es un encabezado <h1> de primer nivel
    ## Este es un encabezado <h2> de segundo nivel
    ### Este es un encabezado <h3> de tercer nivel

Tambien existe una **sintaxis alternativa** para los encabezados que consiste en agregar  
un numero de caracteres `=` equivalente al numero de caracters del encabezado.

    Encabezado nivel 1
    ==================

    Encabezado nivel 2
    ------------------

### Lineas horizontales:  
Con Markdown también podrás lineas horizontales, que resultan utiles para separar el  
contenido o las secciones de un documento.  
Para crear una linea horizontal basta con que agreges tres o más **astericos**, tres o más **guiones** seguidos o tres o más **guiones bajos** seguidos.  

    ***
    ---
    ___

> **Nota:** Es recomendable que dejes una linea en blanco tanto antes como   
> despues de la linea horizontal.  

### Citas:  
Las citas se generan utilizando el caracter mayor que `>` al comienzo del bloque de texto.  
```
> Un pais, una civilizacion se puede juzgar por la forma en que trata a sus animales. -  Mhatma Gandhi
```
*Citas anidadas*

    > Esto es una cita
    >
    >> Esto es una cita dentro de otra cita  

*Citas compuestas*
```
> #### Esta es una cita de ejemplo!
>
> - Me he comprado la PS5
> - Y otro ordenador
>
> *Estare* forever **alone** pero 'Feliz'
```

### Listas: <br>
En Markdown puedes agregar tanto listas ordenadas como desordenadas o para las  
versiones extendidas tambien puedes hacer listas de definiciones.  

*Listas ordenadas*:  
Se agrega un **número** seguido de un **punto**, un **espacio** y un **elemento de la lista**  
La lista no debe estar ordenada numericamente, pero debe comenzar por el numero `1`.   
```
1. Primer elemento
2. Segundo elemento
3. Tercer elemento
```

*Listas no ordenadas*:  
Se agrega un guion `-`, un signo más `+` o un asterisco `*` delante de los elementos de la lista:  
```
- Primer elemento
- Segundo elemento
```
> Nota: Se recomienda usar siempre el mismo delimitador en una lista.  

<br>

*Listas de definiciones*:  
Se debe agregar un **termino** en la primera linea y, en la linea siguiente, dos puntos `:`  
seguidos de **un espacio** y la **definicion** asociada al termino.  
```
Termino 1
: Esta es la definicion del termino 1

Terino 2
: Esta es la definicion del termino 2
: Esta es la segunda definicion del termino 2
```

### Codigos:  
En Markdown tambien puedes definir bloques de codigo, tanto en linea como en forma  
de bloque.  
Para codigo en linea se encierra el codigo entre comillas invertidas \` \`. `<code>`  
```
Cambiar de directorio con el comando `cd`
```
Para codigos en bloque puedes usar:  
Cuatro espacios o una tabulacion: `<pre>`  
```
    let nombre
```

Encerrado el parrafo entre tres `~` virguillas  
```
~~~
Creando codigo de bloque
Puedes añadir tantas linea o parrafos como quieras.
~~~
```

Encerrado el parrafo entres tres \` comillas invertidas  
Tambien puedes agregarle el tipo de sintaxis.
~~~
```javascript
// Creando codigo de bloque
let nombre = "Daniel";
```
~~~

### Tablas:  
Para gregar tablas en Markdown debes definir la cabezera de columna mediante al  
menos **tres guiones** `---` que se situaran por debajo del texto de la cabecera.<br>
Para separar las cabeceras o contenido deberas usar el simbolo de tuberia `|`<br>

```
| Cabecera 1 | Cabecera 2 |
| ---------- | ---------- |
| Elem 1, 1  | Elem 1, 2  |
| Elem 1, 2  | Elem 2, 2  |
```

#### Aliniacion: <br>
Puedes aliniar los elementos de una tabla en el centro, a la derecha o a la izquierda <br>
usando **dos puntos** `:` en uno de los lados.<br>
lado derecho para alinear a la derecha, lado izquierdo para alinear a la izquierda y <br>
ambos lados para alinear al centro.<br>
```markdown
| Nombre  | Tipo  | Color  |
| :-----  | :---: | -----: |
| Manzana | Fruta | Rojo   |
| Pera    | Fruta | Verde  |
```

Elementos en linea
------------------
Un elemento en linea ocupa solo el espacio necesario para su contenido.  


Elementos varios: <br>
-----------------
