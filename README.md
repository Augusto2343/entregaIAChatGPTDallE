                                                                                                 Proyecto Final IA.
Presentación de la problemática: A la hora de comprar o armar una PC hay personas que no saben mucho del tema pero necesitan una PC para poder trabajar, estudiar, jugar, etc.y muchos vendedores se aprovechan de eso para ganar a costa de ellos ofreciéndoles cosas que no necesitan o componentes inapropiados al uso que los clientes le van a dar.

Resolución de la problemática: Esto se puede solucionar si utilizamos bien la IA ya que podemos plantearle nuestro escenario actual ,para que utilizaremos la PC, algunas APPs que usaremos, y cuál es nuestro presupuesto. Para que nos devuelva una recomendación eficaz y acorde a lo que el cliente necesite.

Metodología:
Para generar la lista de componentes: Utilicé chat-GPT y un prompt bien completo para que busque en la web, filtre los componentes con los mejores precios y mejores prestaciones y devuelva los componentes con una explicación corta en formato de lista para que el usuario pueda leerlo y entenderlo fácilmente.

Para generar la imagen: utilicé un modelo texto-texto(ChatGPT4o-mini) para generar el prompt que luego se lo paso al modelo texto-imagen (Dall-e 2) para un mejor resultado.

Herramientas:Utilizaré VS code, ChatGPT 4o-mini y Dall-E 2

Explicación: Voy a consumirlos por medio de la API de openai instalando en mi entorno openai (pip install openai==0.28) y arriba colocando “import openai”, utilizaré una función para generar la conversación  y otra para generar la imagen en la cual le pasé los atributos por ejemplo (model=”dall-e-2”, size=”1024x1024, n=1).

Link al código: https://github.com/Augusto2343/entregaIAChatGPTDallE






Implementación:

Prompt 1: Imagina que eres un vendedor de componentes honesto de una tienda de Argentina y un cliente de confianza que no entiende mucho de tecnología busca una PC. Pregúntale únicamente el presupuesto máximo que puede llegar, para que lo va a usar si quiere algo discreto y si necesita periféricos y En base a eso busca componentes acordes a su presupuesto y uso , luego devuelve los precios y especificaciones básicas para que entienda en forma de lista.


Prompt 2: Presupuesto máximo es de $550 000 y la voy a usar para jueguitos y diseño 3D quiero algo llamativo y necesito periféricos.

Prompt 3:Generame un prompt para generar una imagen con todo los componentes y periféricos que mencionaste antes teniendo en cuenta estos aspectos: dar el tamaño aproximado del teclado y del mouse, agrega que el gabinete tiene que tener los vidrios templados opacos , no describas los componentes internos ni la iluminación, no incluyas marcas, sin mucho detalle, indica la cantidad de cada componente, indica que es una imagen de demostración y el formato tiene que ser un párrafo de texto y en inglés.

Prompt 4 (Creado porChatGPT4o-mini): A demonstration image showcasing a complete gaming and 3D design PC setup. The setup includes one black mid-tower case with opaque tempered glass panels, one 24-inch monitor with a slim bezel, one compact mechanical keyboard (approximately 36 cm wide and 13 cm deep), one ergonomic gaming mouse (approximately 13 cm long and 7 cm wide), one set of over-ear gaming headphones with a built-in microphone, one large mousepad, and a pair of stereo speakers. The arrangement is clean and organized, displaying all peripherals alongside the PC case. No internal components or lighting effects are visible.
 







Resultados:


Herramientas y tecnologías utilizadas: 
Utilicé la técnica de prompting Zero shoot en todos los prompts ya que no le di ningún ejemplo y lo fuí guiando con el prompt que le dí porque si le agregaba un ejemplo se iba a hacer más costoso ya que lo que debe devolver es un listado con los componentes necesarios y las especificaciones y que lo devuelva en una lista por medio de una lista por lo tanto estamos modificando también la respuesta de la IA.


Costo aproximado:
Costo por un 1k de tokens:
OpenAI ChatGPT4o: 0.00125 US$

Tokens:
Tokens de la consigna ChatGPT4o-mini: 91 + 36 +104 =231

Costo:
Costo por imagen 1024X1024 Dall-E 2 : 0.02 US$
Costo en dólares por consulta chatGPT4o: 0,00031 US$
Total aproximado: 0,00037 US$
Tiempo de desarrollo:2 semanas aproximadamente


Justificación de mi elección:Elegí este problema y esta solución porque últimamente está pasando mucho de que la gente que no sabe mucho de componentes se inclina a armarse su pc porque es más viable y menos costoso que una notebook.

La propuesta es económicamente viable ya que utiliza una API externa de chatGPT 4o modelo texto-texto y no debe costar más de US$0.0004 por consulta.  

Por el lado de la  disponibilidad de los recursos e información disponible acerca de los componentes de PC no hay ningún problema ya que hay muchas páginas que especifican las capacidades y características de los componentes.

Objetivos del proyecto:
Utilizar la red para conseguir precios competentes y mostrárselo al usuario
Recomendar lo mejor según el presupuesto y requerimientos del usuario
Darle una idea al usuario de cómo quedaría su “setup” con sus periféricos y su PC por medio de la generación de imágenes.
Ofrecer un consejero de compra de componentes más justo para con los usuarios.

Conclusión:
Logra cumplir con los objetivos propuestos ya que por medio de la IA de OpenAI y por medio de distintos prompts podemos configurarlo y modificar sus respuestas para que sea como un asesor informático y ayudar a los clientes que deseen usar este asistente informático.
Sus puntos fuertes son la generación texto-texto de los prompts y la lista de componentes ya que la generación de imágenes no es tan precisa pero logra cumplir con el objetivo propuesto.

Resultados:
Los resultados de la implementación fueron bastante eficaces ya que la generación de imagen y la generación de texto fueron certeros a la condición actual y el pedido de los clientes.
Logra llegar al resultado esperado ya que se esperaba un asistente en informática que ayude a los clientes a elegir los mejores componentes con respecto a su situación económica y el uso que le iba a dar y hasta incluso genera una imágen de como quedaría su “setup”.


