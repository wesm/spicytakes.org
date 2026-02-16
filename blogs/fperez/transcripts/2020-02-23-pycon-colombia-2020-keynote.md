---
title: "Ciencia Abierta y Comunidades Abiertas"
summary: "Keynote at PyCon Colombia 2020"
date: 2020-02-23T00:00:00
tags: ["talk", "transcript"]
slug: 2020-02-23-pycon-colombia-2020-keynote
word_count: 10809
source_file: transcripts/2020-02-23-pycon-colombia-2020-keynote.md
content_type: transcript
event: "PyCon Colombia 2020"
video_url: "https://www.youtube.com/watch?v=XFynShM1xLU"
---

*This transcript was AI-generated using Whisper and may contain minor errors.*

## Transcript

### Introducción y agradecimiento

Bueno, primero les agradezco mucho a los organizadores. Es un placer y un orgullo estar acá en Medellín. Yo soy de acá, yo soy paisa, y además han montado un evento extraordinario. He aprendido mucho, he conocido a gente muy interesante. Yo soy, hoy en día, profesor en el Departamento de Estadística de la Universidad de California en Berkeley. Y además soy investigador del Laboratorio Nacional de Berkeley, que es un laboratorio del gobierno norteamericano de investigación, ahí al lado de Berkeley. Y soy fundador del Instituto de Berkeley de Data Science, que es un centro de investigación en la universidad.

Y digamos que estoy muy metido en el mundo académico, pero yo llegué ahí de una manera un poco extraña y les voy a contar un poco de qué se trató ese viaje.

### Mentores en Colombia y los primeros pasos

Yo comencé como estudiante de Física, bueno, realmente Ingeniería en la Bolivariana, unos semestres, y me pasé a hacer Física en la Universidad de Antioquia. Hice mi tesis de pregrado con Jorge Maecha, y desde el comienzo tuve la fortuna de tener mentores aquí en Colombia, en la Universidad de Antioquia, de unos estándares intelectuales increíbles.

Alonso Sepúlveda fue mi profesor de Electrodinámica, y estas eran las notas de Alonso, que era un libro hecho a mano, es decir, la copia que uno compraba en la universidad era manuscrita. Y es básicamente una versión, estas son las ecuaciones de Maxwell del capítulo del libro de Alonso, y es básicamente una versión anotada y mejorada del libro clásico de Electrodinámica, con el que después hice el doctorado en Colorado, de Jackson, que además casualmente es un libro escrito por un profesor del Departamento de Física de Berkeley. Y francamente la versión de Alonso era muchísimo mejor que la versión original, y es uno de los cursos de Física y Matemática más elegantes que he visto en la vida.

### Aprendiendo a programar y la lección de perseverancia

Cuando empecé a programar, lo hice en un curso de Física Computacional que dictó el profesor Manuel J. Páez, que además ha escrito uno de los libros clásicos en el tema, en Física Computacional. La tercera edición es en Python, la primera era en Java, la edición actual es en Python y el libro se vende súper bien.

Y Manuel fue un profesor que me enseñó a cómo nunca estar del todo satisfecho con un trabajo y siempre estarlo mejorando, porque yo empecé con un proyecto para graficación de fractales, que era lo que estaba de moda en los 90, en el curso, y era una tarea del curso. Y yo cada que llegaba a la oficina era a mostrarle qué había hecho, me decía, bueno, esto está muy bien, pero falta todo esto y estas ideas, ¿qué más le podría hacer? Y con esa tirita me llevó seis meses y al final me terminé ganando unos premios nacionales con este proyecto.

Tuve la ocasión como estudiante de la universidad de ir a un congreso en República Dominicana, mi primer congreso internacional. Y todo eso básicamente porque Manuel era un mentor que nunca, jamás, me dejaba parar y abandonar una idea media. Y siempre me enseñó a seguirle buscando la punta a las ideas.

### Desconectando a Colombia de Internet

En esa época trabajábamos en PCs, de hecho ese programa de fractales originalmente lo hice en el computador de la oficina de mi mamá, en la Universidad Nacional. Pero estaba llegando el Internet a Colombia y un profesor de física de la Antioquia, Jaime Vélez, fue a trabajar para Conciencias, a montar las primeras conexiones de Colombia Internet, estamos hablando del 93-94.

Se iba a hacer una inauguración de la Conexión Nacional de Internet a Colombia en la Hemeroteca Nacional. Y me dijo, venga, venga y me ayuda, yo estaba terminando el pregrado, venga y me ayuda unos meses a trabajar en esto. Y yo le dije, ¿qué es eso de Internet, qué es? Y me dijo, vea, yo le apuesto un libro para que lea y venga y me ayuda, que usted aprenda rápido.

Y bueno, estábamos trabajando allá, comprando equipos, conectando, haciendo cosas. Y me llama un día un vendedor y me dice, vea, necesito unos cables para conectar un servidor por acá. ¿Usted ha visto dónde habrá un poquito de cable coaxial? Y yo le dije, no, pero claro, espera y verá, yo traigo eso que allí, allí hay una sala donde hay un box que yo creo que no sirve para nada y usa coaxial. Venga, tome.

Y me llaman, me llaman al rato, como a las dos horas, contesto yo el teléfono y me dice una persona, mire, qué pena, yo soy aquí de la estación de satélites, del radiomóvil satelital. Resulta que Colombia está conectado a Internet por una señal que cae en la sabana de Bogotá y hay una antena de línea de vista que le pega a otra antena en el techo de la hemeroteca y ahí se nos está perdiendo la señal, el resto del país está desconectado desde hace unas horas y no sabemos qué pasa. ¿Usted tendrá como alguna idea?

Yo creo que soy de las poquitas personas del mundo que tienen el orgullo de haber desconectado a un país entero de Internet. Porque yo creo que hoy en día eso ya no se puede hacer. Colombia entero estuvo offline gracias a mi genio durante un par de horas en el 93, 94. Yo rapidito fui, me fui para la impresora, imprimí un papel y se lo pegué a ese cable, un papel así que decía jamás, jamás desconectar este cable. Y bueno, no me echaron.

### La frustración de enseñar sin las herramientas correctas

Después de terminar el pregrado, antes de irme a hacer mi posgrado, empecé a dictar un curso en la Antioquia precisamente de física computacional, el mismo curso del que yo había sido estudiante cuando hice ese proyecto de fractales. Y en ese curso yo quería enseñarle a los estudiantes cómo explorar ideas en física y en computación de la manera más interactiva posible. El problema es que yo no tenía acceso a darle a los estudiantes ni Matemática, ni Maple, ni cualquiera de estos sistemas propietarios costosos para toda la clase.

Y lo que terminamos armando fue un monstruo Frankenstein con un box que tenía unas terminales de esas BT.220 que nos permitían usar GNU Plot gráfico conectados a un solo servidorcito que tenía Linux. Bueno, ese monstruo básicamente le sirvió a un estudiante de toda la clase y todos los demás se perdieron por completo en un laberinto de C de errores de punteros, de errores de compilación, de problemas de sintaxis. Y eso nadie aprendió nada y el curso fue horrible.

Y yo me dije jamás, jamás vuelvo a hacer una cosa de estas hasta que no tenga las herramientas correctas, hasta que no haya una manera de hacer esto de una manera mejor. Y bueno, eso se quedó así.

### El doctorado, la crisis y el nacimiento de IPython

Yo me fui a hacer un doctorado en Física en Colorado, en la Universidad de Colorado en Boulder, en Física de Terminación y Física de Partículas. Más que Física de Partículas me pasé mucho tiempo en las montañas haciendo ese tipo de cosas. Y bueno, eso llevó a ciertos problemas. Como por ejemplo que en el quinto año del doctorado mi jefe me echó, mi asesor de tesis me echó, lo cual no es exactamente lo mejor que uno puede hacer en el quinto año del doctorado, eso no es lo ideal.

Y en medio de esa crisis, que me rescató otra profesora del departamento, me dijo, venga, termina este proyectito, a ver si se gradúa y se va para alguna otra parte. Pero en medio de esa crisis lo que me salvó a mí un poco la vida fue, además de que me apoyaron, pues la familia y la esposa, fue precisamente encontrar la Python, encontrar el open source y empezar a trabajar en lo que se convirtió en IPython.

### Motivaciones para crear IPython

Y que fue algo que tenía además, digamos de esas razones personales, una serie de motivaciones que hoy en día para mí siguen siendo muy importantes. Primero, el acceso a las herramientas. Precisamente el poder compartir con, por ejemplo, yo allá en Estados Unidos sí tenía todas las herramientas del caso, tenía todo el software que quisiera, pero si yo quería compartir mi trabajo, por ejemplo, con mis colegas de Colombia, no lo podría hacer si estaba basado en ese tipo de herramientas.

Descubrí además el poder de trabajar con herramientas abiertas para crear ambientes muy colaborativos y comunidades que realmente quieran trabajar juntas. Había un problema para mí epistemológico fundamental y es que la idea de hacer trabajo científico de investigación con herramientas que uno no está legalmente, que legalmente le impiden entender y que alguien le dice a usted, usted puede entender cómo funciona la naturaleza, pero no puede entender cómo funciona su herramienta. Eso me parece completamente absurdo.

Y finalmente que me enamoré del lenguaje, literalmente. Yo había escrito mucho código en Perl, en C++, en Matemáticas, en otras cosas, y descubrí Python y en 24 horas dije, esto es una maravilla, esto es una delicia. Y bueno, me enamoré de eso.

### El primer script y la primera versión de IPython

Escribí la primera versión cuando le dije a mi asesora de tesis a la nueva, a la que sí me estaba ayudando, que le iba a trabajar esto nada más una tardecita. Es un script que lo pueden encontrar en GitHub. En GitHub son 260 líneas de código. Es una cosa diminuta que básicamente es un archivito de configuración como Python Startup.

Y eso llevó eventualmente al IPython que ustedes conocen y que en muchos sentidos se parece a lo que hay hoy en día. Pero el IPython que ya cuando saqué la primera versión después de unas semanas de trabajo, una tarde, desde el comienzo fue un proyecto colaborativo porque yo encontré otras dos herramientas.

Yo empecé a producir, digamos, código para usar Python interactivamente porque lo que yo quería era una herramienta que me permitiera usar el lenguaje para explorar un problema, no para escribir software, sino para mirar unos datos, hacer una gráfica, ver una variable, mirar una tabla, ejecutar, ir iterando sobre un algoritmo. Y ese tipo de proceso de exploración era un proceso que otros dos científicos también habían hecho cosas parecidas.

### La colaboración inicial: Nathan Gray y Janko Hauser

Yo descubrí un estudiante de computación de Caltech, Nathan Gray, y un oceanógrafo en Alemania, Janko Hauser, que ambos simultáneamente habían sacado dos herramientas muy parecidas. Una se llamaba IPP y la otra LazyPython. Y les escribí a los dos y les dije, oiga, yo tengo esta otra cosita que se parece a la de ustedes, que se llama IPython, ¿por qué no juntamos los tres y le trabajamos a hacer algo, digamos, que tenga la unión de los tres proyectos?

Y casualmente ambos me dijeron básicamente lo mismo. Me dijeron, vea, bien puede, haga lo que quiera, use mi código, estoy muy ocupado en otra cosa, pero ánimo. Lo cual es peligroso porque ahí sí se me fueron seis semanas en las que no volví a la universidad, pero fue muy bonito encontrar desde el comienzo, desde la génesis del proyecto, que la gente estaba dispuesta a compartir y a colaborar, aun si en este caso no tenían el tiempo, pero tenían la generosidad de darme sus ideas.

### El primer anuncio público de IPython

Seis semanas después, en diciembre del 2001, este es el mail que lo encontré en estos días con el primer anuncio público de IPython en la lista general de correos de Python. Y hay una cosa que me parece interesante, digamos, mirar de este email original, pues esto fue escrito hace ya casi 20 años, y es que desde el principio decía, sí, el código es un desastre.

Es decir, si ustedes miran lo que hay ahí, porque yo lo que hice fue que agarré mi código con el de ellos dos y armé un zancocho que medio funcionaba, eso medio caminaba para adelante, pero por dentro era un desastre total. Y probablemente si yo hubiera tenido, digamos, más estándares de programación, me hubiera dado pena sacar esto al público.

Pero por alguna razón dije, esto sirve, esto me gusta, esto sirve, lo estoy usando, pongamos esto, entreguémoselo al público porque para el usuario sirve, esto sirve. Esto por dentro es horrible, pero para el usuario, esto a alguien le va a resolver, a mí me resuelve un problema y de pronto a alguien más lo resuelve un problema. Y bueno, entonces se me ocurrió que sería buena idea sacarlo y algún día lo mejoramos.

Y otra cosa interesante es que en ese primer anuncio ya, digamos, muchas de las características que ustedes ven en el IPython de hoy, lo que es, digamos, la experiencia de Jupyter, ya estaban ahí. Es decir, la lista, digamos, como del tanto del objetivo básico del proyecto como de los aspectos básicos de funcionamiento ya estaban ahí en el 2001. Obviamente esto ha tomado muchísimo más trabajo.

### Construyendo la comunidad de Python científico

Para mí lo primero que fue muy satisfactorio fue la reacción de gente como Travis Oliphant que dio un keynote en Bogotá ahora en octubre en SciPy, en SciPy de Latinoamérica. Y que ya desde esa época eran las personas que estaban, digamos, explorando el mundo de Python científico. Y que Travis dice un par de meses después, dice, oigan, ¿por qué no? ¿Por qué no incluimos a IPython como parte de SciPy?

Entonces yo lo que encontré fue, a pesar de que mi doctorado en ese momento era pues un caos total, una comunidad de científicos que dijo, venga, venga, que esto que usted está haciendo nos sirve y nos interesa. Y Janko todavía estaba ahí comentando y también dijo, sí, adelante, sigan con eso a pesar de que yo no esté pues metido en la cosa.

Y un año, bueno, pues en el 2002, finalmente me gradué, terminé, me gradué, empecé un postdoctorado en matemática aplicada. Y lo que pasó fue que en el 2003, Eric Jones, que fue el fundador de Enthought, que fue la primera compañía, digamos, que hizo Python científico, me escribe y me dice, oiga, hay un congreso que se llama SciPy en Caltech, ¿usted por qué no viene?

Yo le dije, vea, yo me acabo de graduar, estoy empezando apenas un postdoctorado, yo no tengo recursos, yo no tengo cómo ir a eso. Dijo, no, no, no, venga, venga, yo lo invito, venga, yo lo invito, venga que SciPy ha resultado muy útil, venga, yo le pago el tiquete y venga para que conozca a la gente y dé una charlita sobre lo suyo.

Y con una invitación así, que para él probablemente, bueno, él era un tipo joven y estaba empezando su empresa, pero pagarle un viaje a un estudiante tampoco es que fuera a quebrar la empresa, me abrió puertas, me abrió puertas y me apoyó.

### John Hunter y Matplotlib

Además, ahí conocí a John Hunter, el fundador de Matplotlib. John y yo nos hicimos, nos volvimos amigos como hermanos y durante 10 años, hasta que lamentablemente él murió en el 2012, trabajamos juntos, los dos proyectos empezaron a colaborar muchísimo y fue parte, digamos, de empezar a crear una comunidad en la cual estos proyectos pudieron ir creciendo.

### El equipo de IPython: Brian Granger y Min Regan-Kelley

Ahora, IPython, aún desde el comienzo, como les decía yo, no solamente fue un trabajo que nació de una colaboración con otras dos personas en el sentido de que me dieron su código, sino que además desde rapidito hubo un equipo. Esto no, es decir, el crédito no es mío, el crédito es de un equipo.

En particular, muchos de ustedes probablemente conozcan, si han seguido la parte científica de Python, a Brian Granger, que casualmente éramos amigos del doctorado. Él también hizo el doctorado en Colorado y empezamos a estudiar al mismo tiempo. En esa época él era profesor en Santa Clara, ahí cerquita de San Francisco. Y Min Regan Kelly, que era un estudiante suyo de pregrado, que luego hizo el doctorado en Berkeley y que luego trabajó conmigo como postdoc en Berkeley.

Desde el comienzo, todos tres físicos, empezamos a trabajar. Ellos se juntaron, se unieron al proyecto más o menos en el 2004. Y una cosa importante es que con ellos en IPython y lo que se volvió luego Jupyter, mantuvimos tanto, digamos, mucho trabajo técnico, como sobre todo con Brian, y de esto vamos a volver a hablar más adelante, mucho de pensar estratégicamente sobre el proyecto. Es decir, qué tipo de cosas hay que hacer a largo plazo en el diseño, cuáles son los problemas correctos en los que se debería trabajar, cómo conseguir recursos, que es algo que va mucho más allá del código. Y yo creo que eso nos ha ayudado mucho, el ser capaz de pensar, el tener un equipo de gente con quien pudiéramos desde el comienzo pensar estratégicamente.

### Una comunidad de amigos y colaboradores

Esto fue, como les decía, toda una comunidad. Esta foto a mí me encanta porque ahí está Wes. Esta fue una foto tomada en el 2012 en la casa, en un asado, en un asado que hicimos en el 2012 en la casa. Y ahí estaban, ahí estaban gente, ahí estaba Travis, estaba Pol Ivanov, que trabaja, es uno de los que trabajan en IPython en Júpiter. Jared Millman, que trabajaba en neurociencia y manejó SciPy varios años. Estefan, que es el creador de Scikit-Image y que ahora está básicamente dirigiendo mucho el trabajo en NumPy. Algunos de los neurocientíficos que trabajan en IPy. Josh Bloom, que es un astrónomo que ha hecho muchísimo por Python en el mundo de la astronomía.

Y es decir, este mundo es una comunidad que fue creciendo de gente que venía, todos de áreas distintas. Hay neurociencia, astronomía, matemática aplicada, visión, trabajan en imágenes médicas, matemáticas, estadística. Francesca Alted, no sé qué formación tiene. Gente que llegó de comunidades muy, muy distintas, unidos todos por el interés de crear cosas juntos, de participar en la creación de cosas juntos y donde se tejieron tanto todo un ecosistema técnico como hilos de colaboración y de amistad que duran hasta hoy en día.

### La relación entre la comunidad científica y la comunidad de Python

Ahora, mientras estábamos en el mundo del Python científico, existía una comunidad mucho más grande que era la comunidad, digamos, de ustedes, de la mayoría de ustedes, de Python, de PyCon. Nosotros teníamos nuestro congresito chiquitico por allá de SciPy y que éramos 100 personas, 150 personas cuando PyCon tenía 1.500 o 2.000, ¿cierto?

Y para nosotros, los científicos, eso ha sido importantísimo porque pudimos aprender mucho de una comunidad mucho más grande, muy sofisticada que tenía no solamente el liderazgo de Guido en el lenguaje, sino trabajo como el trabajo que Jessica McKellar y Carol Willing hicieron en el desarrollo de esas comunidades, el trabajo que Brett y Nick han hecho en mantener, digamos, el equipo central de Python con una dinámica que me parece muy, muy saludable y además con conexiones con la industria el caso de Brett con Microsoft y Nick en Red Hat.

Nosotros, los científicos que estábamos tratando de armar esto todos viniendo de disciplinas distintas, nadie sabe este tipo de cosas, ha sido muy útil tener ese diálogo entre el mundo de nosotros y la comunidad, digamos, de Python más general, más amplia.

### Lo que cada comunidad aporta a la otra

Ese diálogo se expresaba en muchas cosas, no voy a entrar en demasiados detalles, pero por ejemplo, para nosotros poder saber que el lenguaje, hay gente que lo diseña, vimos el keynote de Emily Morehouse en el cual hablaba del trabajo que hizo ella, que hace ella en el centro del lenguaje, el diseño de nuevos operadores, en general, gente como nosotros no sabe de eso y no es necesariamente lo que necesitamos implementar o lo que nos interesa trabajar, pero sabemos, tenemos la confianza de que hay un equipo con gente como Emily que le trabaja eso.

Python tiene una librería estándar con cantidades de cosas que no son estrictamente científicas, pero que uno a veces necesita y si nosotros necesitamos hablar con una base de datos, necesitamos un servidor web, necesitamos un protocolo de red, ahí está, sin que nosotros nos lo tengamos que inventar. Es una comunidad que hace su trabajo en Internet, las cosas tienen que funcionar. Entonces, tiene toda una serie de prácticas de ingeniería de software que nosotros hemos ido aprendiendo y que están muy bien desarrolladas y toda esa maquinaria está muy bien desarrollada.

Una ética de trabajo completamente abierto en Internet que muchas veces en la ciencia, aunque en principio tiene los ideales de trabajo abierto, en la práctica no siempre se comparte tanto como uno quisiera y tiene toda esa estructura de comunidad, del montaje legal de la Python Software Foundation, el manejo de las conferencias y todo eso, ha servido mucho.

Ahora, por otro lado, yo creo que la comunidad científica también le ha contribuido y le ha aportado a la comunidad de Python. Tenemos, hemos producido herramientas que han tenido muchísimo impacto en el mundo y que se usan muchísimo y que han, digamos, elevado el perfil del lenguaje. Hemos educado toda una nueva generación, ahora muchas de las grandes universidades de Estados Unidos, todo lo que es educación en computación y en Data Science se está haciendo en Python y lo que eso significa en estas herramientas, la parte de Machine Learning y Data Science está teniendo un impacto industrial obviamente fenomenal.

El hecho, pues, de que Google, para Google TensorFlow es un proyecto estratégico, para Facebook PyTorch es un proyecto estratégico. Eso viene precisamente de la calidad de Python. Hemos, además, profesionalizado un poco el trabajo en el lenguaje porque nosotros, los científicos, estamos acostumbrados a escribir proyectos, a manejar equipos, a conseguir financiación, a conseguir grants y eso es algo que Emily, por ejemplo, estaba mencionando y es algo que, como Python, apenas lo están empezando a formalizar, nosotros, en ciertos casos, hemos conseguido recursos importantes y yo creo que en ese sentido tenemos algo, digamos, que aportarle a la comunidad central.

Esto es algo que, esta es una cita de Brett, pero que yo creo que es un punto en el que se unen las dos comunidades. Porque es lo mismo que lo dice mucha gente en el mundo de Python, que se encarretó con el lenguaje, pero que llegaron a, digamos, se quedaron con la comunidad. Exactamente lo mismo lo dice la gente en el mundo científico. Y además dice, yo voy a los congresos de mi área en biología, en genómica, en astronomía, en lo que sea. Y es horrible, la competencia es horrible, el ambiente es hartísimo. Pero voy al mundo, digamos, del Python científico y todo el mundo trabaja con un espíritu muy distinto y me encanta la comunidad. Entonces, esa frase es un buen punto de unión, digamos, para las dos comunidades.

### Jupyter: más allá del código

Ahora, Jupyter, digamos, hay Python y ahora Jupyter es un proyecto, sí, es un proyecto de software. Pero yo quiero pensar en esto desde otra perspectiva. Yo creo que en este último año, sobre todo, y crédito a mi colega con la que he desarrollado mucho estas ideas, hemos estado repensando un poco cómo mirar un proyecto de software como algo que va mucho más allá del código. Ignorando, en cierto sentido, el código. Y cuáles son algunos de los otros elementos que a Jupyter le han, que han hecho que Jupyter haya tenido éxito.

Y en ese sentido es pensar que sí, el software es una herramienta, es lo que está en GitHub, es lo que uno instala con Conda, con Pip. Pero para mucha gente lo que interesa son los servicios y el contenido que ese software soporta. Y nosotros en Jupyter nos hemos tomado muchísimo tiempo y le hemos trabajado mucho a abstraer las ideas del software en estándares abiertos, en protocolos bien documentados y en construir la comunidad que soporte todo eso.

Entonces, yo quiero mirar un poco esos elementos y, digamos, alejarnos un poquito del código. Porque si bien uno empieza, cualquier proyecto empieza nada más en su código, lo que realmente le da un impacto a gran escala a un proyecto es pensar un poco en toda esta perspectiva.

### Contenido y servicios sobre el software

Nosotros tenemos cantidades de repositorios. Hoy en día, Jupyter, son como 4 o 5 organizaciones distintas en GitHub. Tenemos como 120 repositorios activos y otros 2 o 300 que están ahí recogiendo maleza. Pero para mucha gente lo que importa es que hay contenido. Que ven en Twitter un link a un artículo, un blog interesante escrito como un notebook. Que pueden acceder a un Jupyter Hub de su empresa o de su universidad para aprender, para tomar un curso. Que encuentran en Binder una manera de ejecutar código sin tener que instalar nada.

Todo eso es la capa, digamos, donde hay una historia, donde hay un servicio que le da algo a la gente. Donde alguien escribió un artículo y analizó los datos con esto. Y lo que le importa a la persona son las conclusiones de ese tema y no cuál era el software o cuál era el código. Y eso toca mantenerlo, además. Es decir, mantener todo ese tipo de infraestructura es un trabajo violento, pero es parte de lo que nos da impacto.

### De software libre a estándares abiertos

Ahora, bajando del software, como les decía, me voy a brincar, digamos, del software, que en cierto sentido es lo menos interesante desde esa perspectiva. Una cosa que nosotros hicimos fue precisamente parar siempre a preguntarnos, bueno, en lo que estamos implementando, en el problema que estamos resolviendo, cuál es la idea que podemos abstraer y que podemos generalizar. Y cómo la generalizamos para que le sirva a otros.

Por ejemplo, originalmente, cuando sacamos la consola de Qt, que ahora la mantiene el equipo de Spyder, fue cuando cogimos lo que era el IPython de la consola y lo partimos en dos procesos. Y dijimos, aquí hay un cliente que puede ser una consola gráfica, en este caso de Qt. Y aquí hay un kernel que ejecuta el código. Y estas dos cosas se comunican por un protocolo. Eso lo podríamos haber hecho así nomás, simplemente implementar eso y dejarlo así.

Pero empezamos a pensar, bueno, ese protocolo, en principio, podría transportar datos en cualquier lenguaje de programación. Y eso los puede transportar sobre una red local o sobre un transporte distinto. Si formalizamos ese protocolo, lo documentamos, lo especificamos bien, esto lo pueden implementar otros.

### Julia, R y el nombre Jupyter

Entonces, trabajamos con el equipo de Julia. ¿Quién aquí ha usado Julia? Por casualidad. Algunos. Un carrete de lenguaje. En este momento es mi lenguaje favorito. Es una maravilla. Si no lo han visto, aprendan un poquito. Es absolutamente encantador.

Entonces, invitamos al equipo de Julia a ver una semana en una reunión de trabajo que teníamos para que empezaran a implementar, después de un prototipo que yo había hecho con ellos un día en el MIT, para que empezaran a implementar un kernel en Julia del protocolo. A ver a dónde llegaban. Llegaron el lunes, el miércoles por la mañana ya estaba funcionando. En dos días tenían funcionando un kernel completamente independiente en Julia.

Luego, un postdoc mío se fue a una reunión de un grupo de R que había en GitHub en esos días en San Francisco. Y yo le dije, váyase y se sienta con esta gente que sabe R. Usted es el que más sabe R de nosotros, que es muy poquito, pero sabe más que los demás. Vaya y les pregunta. Y les pregunta para que le ayuden a ver si podemos tener un kernel de R, de manera que alguien pueda usar toda la maquinaria de Jupyter, pero en otro lenguaje, como R. R es importantísimo en el mundo de la estadística y de la data science.

Y, de hecho, eso fue lo que nos dio la idea de que Julia, Python y R, que son los tres lenguajes abiertos, digamos, de la ciencia de datos y la computación científica, nos daban Jupyter. Nos daban el nombre de un proyecto que no fuera IPython, que fuera una generalización y una abstracción.

Y hoy en día, ya después de que uno hace eso dos o tres veces, la comunidad lo coge. Y hoy en día hay más de 100 implementaciones distintas de kernels de este protocolo. Y eso lo que permite es que crezca todo un ecosistema. Es decir, el tomarse el tiempo para pasar de que aquí hay un software libre a que hay una serie de ideas documentadas, abstraídas y definidas como un estándar abierto, permite que todo un ecosistema crezca y lo mismo suceda a nivel de clientes, etcétera.

### Gobernanza y comunidad

Y, finalmente, mirando la parte de abajo, es que esas ideas no las genera el aire. Esas ideas las genera gente. Esas ideas las generan personas. Y resulta que cuando un proyecto son más de dos o tres personas, manejar el proyecto, manejar la comunidad, entender cómo se relaciona con los empleadores, con las empresas, con quienes lo financian, es todo un problema.

Y nosotros le hemos botado muchísima, muchísima corriente al problema de definir cómo gobernar el proyecto. De hecho, en este momento estamos reiterando, porque el modelo actual que tenemos, si bien nos ha traído hasta aquí, ya llegó a sus límites y estamos rediseñando el sistema de gobierno del proyecto, ha sido un esfuerzo de un año, un año de mucho trabajo.

Pero el habernos tomado el tiempo para empezar a definir que hay un consejo ejecutivo, que hay relaciones formales con, digamos, socios institucionales del proyecto, que tenemos financiación y que buscamos quienes nos financien el proyecto, que tenemos una estructura de apoyo fiscal formal. Yo soy uno de los cofundadores de NumFOCUS. Nos tocó fundar una fundación sin ánimo de lucro que sirviera, digamos, como de organización matriz para todos los proyectos de open source científico.

Todo eso nos ha permitido crear estructuras que van muchísimo más allá de lo que podríamos hacer dos o tres personas colaborando en GitHub. Esto toma mucho tiempo, pero es necesario.

### El proyecto es la gente

Y eso es lo que nos permite finalmente tener lo que realmente es el proyecto, que es la gente, es decir, es la comunidad. No somos dos o tres personas, no es el código, sino un equipo de gente, gente que viene. Si ustedes miran, estas son fotos de dos de las reuniones, digamos, anuales del equipo básico del proyecto. Ahí hay gente de universidades, hay gente de compañías, hay gente de laboratorios del gobierno, hay gente de muchos países, hay gente que contribuye simplemente como voluntarios individuales.

Y precisamente hemos tratado de construir un modelo de comunidad que permita que todos esos actores que tienen necesidades distintas, intereses distintos, recursos distintos, puedan trabajar, puedan trabajar juntos y puedan mantener el resto de la comunidad abierta.

### Invitación a la comunidad latinoamericana

Y yo digo todo esto porque lo que quiero es hacerles una invitación a todos ustedes, una invitación especialmente a Latinoamérica. Esto lo ha liderado mucho otro de los presentadores de un Keynote en SciPy, que se llama Damián. Damián es un ingeniero que en ese momento trabajaba en Anaconda y es un argentino que ha estado trabajando mucho para fomentar la comunidad de Júpiter en América Latina. Una comunidad en la cual todo tipo de contribución, código, documentación, trabajo, participación en proyectos educativos, traducciones, lo que sea, sean igualmente valoradas y reconocidas.

Y lo que Damián ha estado haciendo es conseguir recursos para organizar talleres. Este fue el primero, que fue el año pasado, en Córdoba, en la Argentina, y creo que este año va a haber otro. Como parte de un programa que tenemos con financiación de Bloomberg y de Amazon, tenemos un programa para talleres comunitarios alrededor de Júpiter.

Esta es, por ejemplo, la lista de los talleres que se hicieron el año pasado. El de abajo es el que Damián organizó para desarrollo en la Argentina. Yo veo que la comunidad de Python de Colombia es fabulosa, es grande. Este es un evento enorme, este es un evento con 500 personas. Yo lo que quiero es, digamos, invitarlos, invitarlos a que se unan, invitarlos a que participen, invitarlos a que se conecten.

### Talleres comunitarios: de centros de supercómputo a niños en Inglaterra

Y este esfuerzo, digamos, de hacer talleres para la comunidad es una manera en la cual tratamos de crecer el proyecto en direcciones distintas. Si ustedes ven la lista de talleres ahí, hay cosas, por ejemplo, este, el cuarto, fue un taller que hicimos en Berkeley, muy, muy técnico de laboratorios, digamos, científicos grandes, organizaciones de investigación grandes, la Agencia Espacial Europea, centros de supercómputo.

El primero fue una introducción a programación para niños en la parte más pobre de Inglaterra. Y uno piensa que Inglaterra como un país rico, ¿no? Pero eso es una región tan, tan pobre, que como parte de los fondos que nos pidieron los organizadores, nos pidieron que si les aceptábamos usar una parte de los fondos para comprar unos 20 laptops del más barato que venden para poderle dar a los niños. Porque es una parte tan, tan, tan pobre en Inglaterra que nadie tiene computadores y querían por lo menos poderle enseñar, tener una sala en la cual usaban Python y tener un taller para enseñarle a niños a programar.

Entonces, es como por mostrarles un poco que con los recursos que tenemos y con este tipo de colaboraciones institucionales tratamos de hacer cosas que hacen crecer el proyecto en direcciones muy distintas, ¿cierto? Centros de supercómputo, laboratorios nacionales de investigación o niños en la región más pobre de Inglaterra. Y hay un eje de eso, es hacer crecer la comunidad latinoamericana. Y espero que eso continúe y que se pongan en contacto con Damián y obviamente conmigo.

### Resumen: las capas del impacto

Entonces, en resumen, digamos que si uno lo mira desde esta perspectiva, estas capas a lo que nos muestran es que sí, el software es importante y hay que estudiar código. Y eso es en muchos casos lo que a uno le gusta. Pero el impacto llega cuando con ese software la gente hace algo. Cuando la gente, en nuestro caso en general, termina produciendo historias alrededor de computación, datos, análisis y entender problemas.

Tomarse el tiempo para distinguir cuáles son las herramientas concretas de las ideas generales, lo que nos permite es empezar a dar el tejido intelectual de un ecosistema. Un ecosistema que pueda crecer y en el que otros puedan participar con sus propias ideas.

Y finalmente, si eso realmente uno lo logra anclar sobre una comunidad saludable, de ahí es donde vienen las ideas nuevas, donde viene la innovación, donde viene la resistencia, digamos, al cambio, a que si sea una persona de por acá habrá otra persona que llegue con nuevas ideas. Y yo creo que es importante cuando se habla de Open Source, cuando se piensa en esos proyectos, ver un poco esta perspectiva, digamos, más general.

### El ecosistema: nadie lo hace solo

Todo esto es en un ecosistema enorme. Es decir, yo no solamente no quiero que nadie crea que el crédito de esto es mío dentro de Jupyter, sino que además el crédito de Jupyter no es de Jupyter. El crédito de Jupyter es Pandas. Es decir, si no fuera por Wes, mucho de esto no había tenido el impacto que hemos tenido. Si no fuera por John Hunter, que se pasó años creando Matplotlib, por la gente que se la pasó creando NumPy, SciPy, por el equipo que desarrolla Python mismo, que es, digamos, la base en la que estamos montados.

Este es un ecosistema en el que todos dependemos los unos de los otros y eso es lo que hace a Python una herramienta tan poderosa.

### Spyder: colaboración entre proyectos

Dentro de ese ecosistema hay proyectos que colaboran los unos con los otros. El ejemplo de Spyder es un ejemplo fabuloso. Ya vieron una pequeña lightning talk de ellos. Acaban de sacar la versión 4. Resulta que Spyder tiene pedazos de IPython. La consola de Qt ahora la mantiene el equipo de Spyder. Tiene soporte para los notebooks dentro de Spyder.

Y si bien Carlos Córdoba es el líder del proyecto, que muchos de ustedes lo conocen, resulta que aquí tuve la fortuna de conocer a todo el equipo. Y que no solamente era un colombiano, sino un grupo de colombianos los que ahora dirigen Spyder. Además, es un proyecto que es una cosa fabulosa. Es uno de los proyectos, yo creo, que en el mundo de open source con mejor internacionalización, disponible en muchos idiomas. Vamos a ver si encontramos cómo colaborar con ellos en eso, porque en eso nos llevan kilómetros a Júpiter. Entonces, vamos a ver si podemos encontrar la manera de trabajar con ellos para, en ese sentido, mejorar a Júpiter.

### Impacto en la investigación científica: ondas gravitacionales

Entonces, basados un poco en estas ideas, quiero hacerles una rápida mirada, por lo menos, de qué tipo de impacto han tenido estas ideas y estas herramientas construidas de esta manera en el mundo donde yo me muevo, que es el mundo de la investigación científica y de la educación.

No sé si algunos de ustedes hayan visto que el Premio Nobel de Física en el 2017 fue por la primera detección de las ondas gravitacionales. Eso fue, se le otorgó al equipo que logró observar la colisión de dos agujeros negros. Y esta figura es una figura de, es la figura número uno en el paper principal de esa observación. Esto va a ser una de las figuras más citadas en la literatura de la física por los próximos 50 años.

Para nosotros esa figura es fuente de muchísimo orgullo, porque todas esas gráficas fueron hechas con NumPy, con SciPy. Las gráficas son, bueno, las gráficas son esas con Matplotlib. Cuando nosotros estábamos creando todo esto, nos dijeron explícitamente, dejen de hacer esto, esto es una perdedera de tiempo, esto no sirve para nada, esto no es trabajo de verdad, etcétera, etcétera, etcétera. Es decir, nadie nos apoyaba, nadie nos financiaba, nadie, la gente nos decía que no lo hiciéramos.

Y saber que uno de los resultados más importantes de la física de los últimos años, pues, parte de la investigación se hizo con esto, es increíblemente satisfactorio.

### Binder: ciencia reproducible sin instalar nada

Y el equipo que sacó eso, además, publicó todos los notebooks del análisis. Cualquiera de ustedes puede ir a este link y puede, por ejemplo, vamos a ver si el audio funciona. ¿Se oyeron ese pequeño whoop? Ese es un cuarto de segundo en el cual dos agujeros negros, más o menos, con un total de 60 masas solares, terminan colapsando el uno dentro del otro y escupen, creo que, unas tres masas solares en forma de energía pura, como ondas gravitacionales. Eso es lo que se detectó en esos detectores y eso es lo que se ve aquí. Ese aumento de frecuencia, eso va sonando whoop. Entonces, ese es literalmente el sonido, la sonificación de dos agujeros negros colapsando, gracias a todo el ecosistema que lo podemos ver, gracias a todo este ecosistema.

La razón por la cual cualquiera de ustedes puede ejecutar ese código en su teléfono es un proyecto que se llama Binder, que es un proyecto, digamos, derivado del mundo de Jupyter que les permite coger cualquier repositorio de Git público, en Git o en cualquier cosa, y mientras ese repositorio tenga las dependencias listadas, el sistema lo coge, lo compila, arma una imagen de Docker y les devuelve una URL ejecutable.

Eso originalmente nos motivó a crear ese proyecto, el poder compartir cosas como eso. La literatura científica, de manera que alguien pudiera repetir un análisis, ver un resultado sin instalar nada, sin tener acceso a herramientas, a nada. Pero se ha vuelto una herramienta muy útil para simplemente compartir cualquier código, para demostrar cualquier software y compartir cualquier contenido, digamos, contenido computacional.

### La primera imagen de un agujero negro

Otro, más recientemente, muchos de ustedes puede que hayan visto esta imagen porque esta imagen le dio la vuelta al mundo. Esta fue una charla por el director del proyecto, Shep Doeleman, en Harvard. Al otro día del anuncio público resulta que tuvimos la buena suerte de que la primera charla pública que ellos dieron, la dieron en Berkeley, en el Departamento de Física. Entonces logré verla.

Y Katie Bouman, que es la directora, que ahora está en Caltech, que es la directora de la parte de análisis de imágenes, también dio una charla. Yo lamentablemente no la pude ver. Me sacaron del auditorio y me tocó verla de afuera. Mi papá así se logró entrar. Le tocó la última silla en el auditorio a él. A mí me tocó verla desde afuera porque el auditorio estaba completamente lleno.

Y ellos, cuando dieron el primer anuncio público con estas conferencias en Berkeley, bueno, sacaron el anuncio de prensa el día antes y luego fueron a Berkeley a dar las conferencias, incluyeron en los artículos científicos de la observación, de la primera foto, digamos, de un agujero negro, las citas a todos los paquetes del ecosistema científico. Ahí está Pandas, ahí está Matplotlib con John, ahí estamos nosotros con Júpiter, reconociendo el valor de esta comunidad.

### 23 mil contribuidores detrás de un descubrimiento

Unos meses después me vi con Katie en Suiza, ahora en octubre, donde estamos dando una presentación y ella, después de hablar, digamos, del trabajo científico, paró a mostrar esto. Esa imagen es un análisis del gráfico de dependencias, digamos, de todas las librerías de ellos y qué alimenta el código de ellos en GitHub. Ese análisis originalmente lo hizo GitHub para ella, la gente de GitHub hizo ese análisis para ella, pero ahora esa herramienta, ya uno puede correr ese cálculo sobre cualquier proyecto, GitHub publicó la herramienta.

Y aquí, es decir, si uno hace zoom en esta foto, ahí van a ver los nombres de mucha, mucha gente, de muchos, muchos de estos proyectos que les mostraba. Y suma más o menos, por lo menos sumando commits, 23 mil personas. Es decir, lo que Katie estaba reconociendo ahí es que ese trabajo, el código, ese estudio que es uno de los, eso va a ser seguramente otro premio Nobel en física, es posible gracias a 23 mil personas como ustedes, como nosotros, que han producido código open source y que lo han contribuido en GitHub y todo, además todo en Python, porque toda la maquinaria de ellos es en Python.

### Pangeo: ciencia interactiva en la nube

Este es un ejemplo de un proyecto nuevo en el que estamos ahora trabajando para hacer ciencia en la nube. Voy a poner un pequeño videíto, un segundito, y lo que van a ver es una cosa que no tiene mayor misterio. Yo hago clic ahí, es una imagen, y van a ver que alguien le hace como zoom a la imagen y cuando hace zoom empiezan a verse cosas de colores abajo y al ratico pasan unos segundos y la imagen como que refina la resolución.

No tiene nada raro. Lo mismo que uno hace en el teléfono. Le hace zoom a una foto y la foto al momentico se ve mejor. Resulta que esa imagen son 100 gigas de imágenes satelitales sobre el estado de Washington y los colorcitos de abajo es un clúster grandote que tiene que analizar todo eso para regenerar una imagen de mayor resolución sobre esos 100 gigas de datos.

Eso es un trabajo, digamos, de mucha ingeniería. Es ingeniería de nube, es cálculo distribuido. El científico que quiere analizar eso, la persona que lo único que quiere es pensar en el problema de los datos, esa persona no tiene por qué volverse una ingeniera de nube. Esa persona probablemente, en este caso, es una persona que hace geofísica, geociencia, y su trabajo debe ser pensar en la ciencia, no volverse una ingeniera especializada en Google o en Amazon.

Entonces Pangeo es un proyecto que agarra Jupyter, agarra Dask para computación distribuida, agarra X-Ray para la representación de los datos y pone todo eso en la nube precisamente para permitirle a comunidades científicas trabajar en la nube sobre grandes volúmenes de datos.

### Analizando datos climáticos desde el teléfono

Hace un par de días esta persona puso en Twitter esto diciendo, estoy analizando el CMIP6 en el tren usando mi teléfono. ¿Qué significa CMIP6? CMIP6 es el conjunto de datos que alimenta los análisis del panel intergubernamental de cambio climático que produce unos análisis cada cierto número de años, que son los análisis que llevan a los acuerdos globales de cambio climático. Ese conjunto de datos va a llegar probablemente cuando esté completo a 30 petabytes. Eso nadie lo va a poder bajar, eso no cabe en ningún computador, es decir, eso solamente lo vamos a poder estudiar si tenemos herramientas de este estilo en la nube.

Ya han salido parte de los datos, con Google hay una colaboración para que esos datos estén en la nube de Google y con estas herramientas, en un teléfono, esta persona estaba desde el tren analizando eso. Ese es el tipo de impacto científico que queremos tener.

Nosotros estamos trabajando ahora, acabamos de recibir un grant nuevo de la Fundación Nacional de Ciencia, precisamente junto con Joe Hamman, que es uno de los directores de Pangeo, y con un equipo de Berkeley, para trabajar en tres problemas de geociencia junto con seguir desarrollando Júpiter, precisamente en este espacio, digamos, de ciencia interactiva abierta en la nube. Estamos muy contentos, estamos empezando a contratar gente, estamos apenas arrancando.

### ICESat-2: contando fotones con Python sobre la Sierra Nevada de Santa Marta

Otro proyecto que estamos arrancando es una colaboración con dos glaciólogos, glaciólogistas, yo no sé cuál será la palabra en español, dos personas que trabajan en criociencia, para desarrollar herramientas para trabajar con un satélite nuevo, un satélite que acaba de mandar la NASA, que se llamaba ICESat-2, que es un satélite de LIDAR, es decir, es un satélite que manda un láser, un láser que se parte en tres, y cada uno de los tres se vuelve a partir en dos, entonces son seis láseres verdes que le pegan, que van barriendo la Tierra, y es un proyecto nuevo, la NASA apenas lo mandaron, empezó a producir datos en mayo del año pasado, y lo que queremos es crear toda la maquinaria en Python, que sea abierta para el análisis de estos datos.

Todavía no nos han contestado de la NASA si nos dan los fondos, pero ya el proyecto está arrancando, y Jessica, que es como la programadora principal del proyecto, junto con este estudiante, Shashank, ya produjeron uno de los primeros ejemplos, es sobre Colombia.

Yo no sé si ustedes saben que la Sierra Nevada de Santa Marta es un poquito un misterio geológico, porque no es parte de los Andes, y es el gradiente de elevación más fuerte que hay en el mundo al lado del mar, y de hecho el gradiente sigue hacia abajo muchísimo, es un gradiente brutal que no es volcánico, y que está completamente aislado, y desde el punto de vista geofísico es un poquito un misterio.

Pero resulta que estos son los datos que están abiertos y que con esta librería los pueden, cualquiera de ustedes puede bajar eso y correrlos, y ver, bueno, cuál es la estructura de la Sierra Nevada. Resulta que a medida que el satélite va pasando, va barriendo, va barriendo, ahí se ven, digamos, los tres dedos del satélite, y eso, que son, que este es, digamos, como la caricatura de lo que está pasando, bajamos esos datos, escogemos qué parte queremos mirar, y podemos tener, este es el perfil, digamos, de elevación de la Sierra Nevada de Santa Marta contando fotones con Python, literalmente contando dónde, de todos los fotones que bajan del láser, cuáles rebotaron, cuáles llegaron y volvieron a pegarle al satélite, cuáles bajan hasta la tierra y vuelven a pasar por el lente del fotodetector, y tenemos, podemos ir viendo la estructura de elevación de la Sierra Nevada.

### Herramientas de investigación como herramientas educativas

Ahora, estas herramientas de investigación tienen un impacto educativo, y una de las cosas importantes del ecosistema de Python precisamente es que las mismas herramientas de educación, este es un proyecto de geofísica desarrollado por un equipo canadiense y una colega que también fue keynote speaker en el SciPy de octubre, que fue desarrollada para problemas inversos en geofísica, pero, es decir, para entender cómo es el subsuelo de la tierra usando datos sobre todo electromagnéticos aunque también datos de gravedades magnéticos.

Resulta que ese proyecto de investigación, ellos han estado, empezaron a desarrollar materiales, notebooks interactivos con widgets para poder explorar los modelos, porque correr esos modelos y estar cambiando 25 parámetros aún en investigación es mucho boleo. Entonces, a medida que empezaron a desarrollar widgets para investigación, resulta que lo que tenían era una excelente herramienta educativa. Es decir, pueden enseñar problemas en geofísica con la herramienta de verdad de investigación.

Con esa herramienta montaron entonces un proyecto que se llama Geosci.xyz, con el cual tienen montado un curso de geofísica que han dictado por todo el mundo, y que publica unos como apps, precisamente para explorar problemas interactivamente con Júpiter en geofísica, que además corren sobre el mismo Binder, el mismo Binder que les contaba. Cualquiera de ustedes, si les interesa aprender un poquito de esto, va acá, hace clic en este link, launch binder, y Binder les ofrece inmediatamente un notebook con estos widgets en los que pueden empezar a leer, bueno, a leer del tema, si les interesa, y a explorar los modelos.

### Jupyter Book y la educación en Berkeley

Eso nos está dando la maquinaria para producir textos y materiales educativos de una manera que hace 20 años, precisamente era lo que yo quería y que no tenía.

Hay otro proyecto en el ecosistema nuestro que se llama Júpiter Book, que acaba de recibir un grant nuevo, lo dirige Chris Holdgraf, un investigador que trabaja también conmigo en la universidad, y que es para poder publicar fácilmente y con poco esfuerzo una colección de notebooks como un libro, como un material educativo interactivo.

Esta es una imagen de uno de los libros de ciencias de datos que usamos en los cursos de Berkeley. Resulta que en Berkeley tenemos un nuevo pregrado en ciencias de datos, cuyos cursos han sido los cursos que más rápidamente han crecido en la historia de la universidad.

Este es el año pasado, este libro que les mostraba acá, es para un curso que se llama Data 8, que se llama Fundaciones de Ciencias de Datos. El libro ustedes lo pueden ejecutar también con Binder, si ustedes van a este link, en cualquier capítulo pueden hacer clic en interact, y les abre precisamente un Binder en el cual pueden correr el libro.

### Llegando a toda la universidad

Y con estos cursos le estamos llegando básicamente a toda la universidad. Yo nunca he dictado Data 8, que es el más grande, es el de primer semestre. Es un curso que le enseña a las personas, a los estudiantes de primer semestre, sin ningún requisito de programación, a empezar a analizar datos y a hacer inferencias estadísticas usando Python. Este curso que sí lo he dictado, es el de Data Science, es un curso digamos de sexto semestre más o menos de universidad, ya con un poco más de matemáticas, de álgebra lineal y de cálculo.

Pero con estos cursos lo que podemos hacer precisamente, es resolver el problema que yo tenía hace 30 años. Es decir, esa porquería, ese horror de que los estudiantes se perdieran, nos demoramos 30 años, pero ya, ya tenemos, tenemos los notebooks, tenemos los materiales educativos, tenemos un Jupyter Hub, que cualquier estudiante de la universidad, simplemente con la identificación de la universidad, encuentra los servidores preconfigurados, para poder enseñarle literalmente a toda la universidad. Con estos cursos ya le estamos llegando más o menos a la mitad, a la mitad de la población universitaria, en este momento.

### Pedagogía con Jupyter

Y esto ya se está convirtiendo en algo en el cual, ahora lo que nos toca es pensar, cuáles son las mejores prácticas pedagógicas. Con este mismo apoyo de esos talleres, Lorena Barba y otro grupo de personas, organizaron un taller hace un año, que se llamaba precisamente Cómo Enseñar y Aprender con Jupyter. Y lo que hicieron fue publicar un libro online, digamos de prácticas pedagógicas, para que no tengamos todas las soluciones.

Lorena es una profesora en la Universidad de George Washington, es una profesora, es una chilena, que es profesora de Ingeniería Aeroespacial en George Washington. Trabaja en métodos numéricos y organizó este evento, digamos, con otros educadores que enseñan en distintas áreas, para intentar pensar, bueno, qué es lo bueno y lo malo de trabajar con Jupyter en un contexto educativo, qué problemas tenemos que resolver. Y sacaron un libro, que es básicamente una colección, digamos, de patrones pedagógicos.

Y una de las cosas que a mí más me gusta de ese texto es que plantearon el problema del aprendizaje como un diálogo que tiene que ir en ambas direcciones. Y en este caso, sí, hay mucha computación y siempre estas son herramientas para hacer computación, pero es una computación que en esa conversación puede jugar distintos papeles. Hay veces que el lugar de la herramienta computacional es enseñar, por ejemplo, física, ¿cierto? Entonces, de lo que se trata es de darle a las personas algo en lo cual se puedan concentrar en la pregunta, en la idea, en el fenómeno físico, o en el algoritmo, o en el problema numérico, ¿cierto? Pero no en la programación.

Una cosa que sostenga un diálogo entre seres humanos, es decir, entre personas que están intentando entender un problema juntos. Pero a veces, de lo que se trata es de usar un ejemplo, digamos, puede ser físico, para motivar, sí, la enseñanza de programación, la enseñanza algorítmica. Y en esa dialéctica, digamos, podemos aprender ambos lados.

Y con esta maquinaria, realmente, eso sí se puede hacer. Es decir, esa frustración tan horrible que yo tuve en la de Antioquia en el 93, 94, realmente por fin tenemos como atacarla.

### Enseñando con herramientas reales, no con juguetes

Yo espero, digamos, que con eso tengan un poco una perspectiva de que con estas herramientas sí estamos realmente teniendo un impacto grande, tanto en investigación como en educación, y además en esas dos cosas juntas. Porque no estamos enseñándole a los estudiantes con jugueticos. Es decir, no les estamos enseñando con una cosa de juguete que después cuando salgan al mundo real la tienen que abandonar, sino que les estamos enseñando literalmente con las mismas herramientas que los investigadores escribieron para sus propios problemas.

### JupyterLab: reimaginando la experiencia interactiva

Ahora, nosotros seguimos desarrollando cosas. Les quiero por lo menos rápidamente mostrar que toda la maquinaria del Notebook ahora la hemos un poco reimaginado en un proyecto que se llama JupyterLab. La versión 2 está a punto de salir. Esto ha sido un trabajo de equipo muy grande que ha tomado mucho tiempo, con participación también de la industria.

Y rápidamente la idea de JupyterLab es repensar un poco, bueno, cuáles eran todas las cosas que teníamos en la experiencia interactiva de hacer cálculos, de tener Notebooks, de correr código, de explorar datos, y cómo podemos crear una infraestructura que haga que todos esos elementos estén ahí disponibles, que sigan soportando las cosas que hacíamos antes. Es decir, un Notebook se puede correr como antes, pero que yo pueda tener esas cosas hablando las unas con las otras.

Por ejemplo, que yo pueda tener un Notebook aquí, pero que la visualización que tengo acá la pueda tener disponible en otra parte y estén sincronizadas, de manera que si necesito mirar otra parte del documento, pueda seguir viendo esta visualización. Que pueda ver ese mismo Notebook como un documento PDF. Que si lo que necesito es ver unos datos, yo pueda directamente ver una imagen, yo pueda ver directamente una tabla.

O por ejemplo, que yo pueda decir estos datos, ahí no se ve mucho, pero eso es JSON, resulta que eso es JSON en un formato de información geográfica. Eso no es JSON normal, sino que es GeoJSON. Y el GeoJSON es, digamos, una estructura de JSON para codificar información geoespacial. Obviamente la información geoespacial es mucho más sabroso verla en un mapa. Entonces, uno puede coger una tabla de GeoJSON y abrirla, los mismos datos como mapa.

Y en el momento en que estos elementos estén ahí en el sistema, cualquiera de ellos puede aparecer en otra ventana, puede aparecer en un Notebook, se puede visualizar programáticamente. Entonces, la idea era poner todos los pedacitos, digamos, la terminal, el manejador de archivos, el manejador de documentos, los editores de texto, como, digamos, piecitas de Lego con las cuales la comunidad pueda armar nuevas soluciones y que se estén comunicando precisamente con los protocolos y los estándares del proyecto.

### FlyBrainLab: JupyterLab para neurociencia

Una cosa que nos produjo muchísima satisfacción fue descubrir hace poco esto. Esto es un proyecto que se llama FlyBrainLab, creado por el laboratorio de un profesor en Columbia que se llama Aurel Lazar. Y lo que hicieron fue precisamente crear una versión de JupyterLab, pero que le agregaron ellos. No es GeoJSON, no son simplemente imágenes, sino un navegador para ver modelos en tres dimensiones de la anatomía de la mosca.

Resulta que los circuitos neuronales que el usuario quiera analizarlos puede simular como un circuito electrónico. Entonces, es ejecutar una simulación de circuitos corriendo en un clúster de GPUs y luego puede acceder a la información de genómica sobre ese circuito, porque también tiene una base de datos especializada en genómica, pero todavía tienen los notebooks de toda la vida.

Entonces, lo que hicieron ellos fue decir, bueno, con estas herramientas de Lego tenemos el básico de un ambiente de trabajo para exploración de la genética, la anatomía y las conexiones neurológicas de la mosca, que es uno de los organismos básicos en neurociencia, porque se reproducen muy rápido y se les puede hacer mucha cosita. Y con eso armaron un nuevo entorno de trabajo científico, que es la base abierta de JupyterLab y una serie de plugins que ellos los desarrollaron. Obviamente nosotros no vamos a desarrollar una herramienta de esas, es una cosa muy especializada, pero le permite a cada comunidad científica empezar a armar sus propias herramientas basadas en los estándares generales.

### Infraestructura a escala nacional: el modelo canadiense

Ahora, esos son equipos de investigación, pero resulta que con esto también podemos desplegar infraestructura a gran escala. En Berkeley nosotros lo estamos haciendo a nivel de toda la universidad, pero en el Canadá lo están haciendo a nivel de todo el país.

Resulta que un equipo del Instituto de Ciencias Matemáticas del Pacífico lo que hizo fue armar un proyecto para desplegar, un proyecto que se llama CCG, que le ofrece a cualquier investigador del Canadá, en los clústeres de una cosa que se llama Compute Canada, que es como el recurso de cálculo para investigación en Canadá, les ofrece ambientes de Jupyter, como los que nosotros tenemos en la universidad, pero para cualquier investigador canadiense.

Y luego se juntaron con la directora de esta empresa, que se llama Cybera, para además ofrecer eso mismo para educación, desde creo que desde kinder hasta bachillerato. Entonces ahora, por un lado tienen el proyecto de investigación y por el otro lado tienen el proyecto educativo y le ofrecen, digamos, desplegar estos recursos a cualquier educador o investigador en el Canadá. Ojalá tuviéramos algo así en Estados Unidos, ni modo, porque eso es un desastre. De pronto aquí en Colombia en algún momento se podría pensar en ofrecer este tipo de infraestructura en la educación y en investigación.

### Relación con la industria

Y de todos modos yo quiero mencionar que el proyecto colabora con la industria, es decir, yo trabajo en un mundo académico, en el mundo científico, yo sigo trabajando como docente y como investigador, pero Jupyter mantiene conexiones con la industria y además es usado, no solamente lo usan compañías, sino que hay productos. Es decir, Google tiene varios productos basados en Jupyter, Microsoft tiene los notebooks en Azure y de hecho en estos días acabo de ver que sacaron una nueva cosa en .NET, como una nueva iteración con apoyo en .NET para los notebooks. Anaconda tiene productos basados en Jupyter, Amazon tiene SageMaker, que es básicamente la plataforma de Machine Learning que usa Jupyter.

Y eso está muy bien, es decir, mantener una relación saludable con las grandes empresas no siempre es fácil. Como mencionaba Emily en su Keynote, la financiación de esto, de empresas tan grandes, todos quisiéramos que fuera un poco mejor. Wes también habló mucho del tema y ese es un tema que a todos nos tiene sufriendo mucho, porque estas empresas no siempre contribuyen tanto como quisiéramos. Pero bueno, es un diálogo en el que seguimos tratando de mantener como la mente abierta y encontrar la manera de cooperar, de cooperar de manera más productiva con ellos.

### Agradecimientos y financiación

Finalmente, quiero, para dejar tiempo para discusión, dar las gracias a los que nos han dado recursos, porque este proyecto, como les decía, no existiría si no fuera porque a lo largo de los años nos han financiado y además porque lo hemos buscado. Y este es el tipo de cosas que yo creo que la comunidad de Python está empezando a hacer un poco mejor, pero nosotros hemos hecho mucho trabajo durante los últimos 10 años sobre todo en conseguir recursos tanto de fundaciones privadas como del gobierno americano como de compañías de distintas maneras.

### Mensaje final: orgullo colombiano y valores de la comunidad

Y bueno, quiero entonces cerrar un poco en resumen como con un mensaje. Primero de que yo soy vivo, muy orgulloso de ser colombiano, además porque todo lo que he hecho lo hice gracias a lo que me dieron acá, a los mentores que me dieron las bases y las herramientas intelectuales para salir sin el más mínimo, digamos, sin la más mínima sensación de ninguna limitación a trabajar con la comunidad internacional en este contexto, que además fue una comunidad que me recibió de brazos abiertos, que me apoyó, en la cual encontré gente en el mundo de Python científico que todas quería hacer lo mismo, trabajar juntos, colaborar, cooperar, crear cosas juntos.

Logramos con esa comunidad, ahí son gozorongo, eso ha tomado tiempo, pero hemos tenido un impacto realmente grande, a pesar de que a muchos de nosotros no nos apoyaron, muchos de estas personas se quedaron sin trabajo. Esta es la historia del éxito, ahí hay muchas historias malucas y hay mucha gente que hizo sacrificios muy difíciles, pero hemos logrado tener un impacto muy importante.

Y yo sigo convencido de que a pesar de las dificultades, este es el tipo de valores, este es el tipo, digamos, de formas de trabajar, que es el mismo mensaje que dio Emily, es el mismo mensaje que dio Wes, de cooperación, de colaboración, de interdisciplinas entre comunidades geográficas, entre comunidades intelectuales, con los cuales podemos realmente tener, atacar los problemas que tenemos en la sociedad hoy en día.

### Cierre y JupyterCon 2020

En las camisetas de los voluntarios vi que tenían Coding and Dreaming, creo que era el eslogan de ustedes y me encantó, me encantó absolutamente.

Yo le doy, para mí, las gracias son al equipo, al equipo de Júpiter, que obviamente nada de lo que yo he hecho hoy en día sería posible si no fuera porque todos ellos son los que hacen el trabajo, entonces a ellos es a los que les debo, digamos, mucho de lo que han visto hoy.

Y finalmente les quiero, a los que no lo vieron en Twitter, les quiero comentar que acabamos de anunciar la nueva edición del Congreso de Júpiter, de JupyterCon, que va a ser en Berlín del 10 al 14 de agosto y Lorena, quien nos albergó esa foto anterior, era tomada en el laboratorio de ella, Lorena, esta mujer excepcional, una científica chilena excepcional, profesora en Washington, va a ser quien va a dirigir la conferencia.

Yo lo hice los primeros dos años, eso es mucho trabajo, yo le agradezco muchísimo a los organizadores porque sé que sé lo duro que es el trabajo de hacer un evento de estos y Lorena va a liderar el desarrollo de la nueva JupyterCon. Acaba de salir la llamada a Reviewers, cualquiera de ustedes puede ayudarle al proyecto revisando algunas propuestas, revisando papers, las formas están en Twitter, salieron hace un par de horas y bueno, espero ver a muchos de ustedes en Berlín y también por aquí en Medellín obviamente, espero seguir conectado con la comunidad de Python colombiana.

Muchísimas, muchísimas gracias por la invitación, por su atención y por quedarse aquí hasta el final, después de tres días largos de mucho trabajo, yo sé que todos están muy cansados. Muchas gracias.
