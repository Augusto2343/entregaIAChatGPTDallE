Proyecto final de IA generación de prompts 
Este asistente que integra IA de OpenAI (chatGPT4o) te ayudará a elegir los mejores componentes de PC para el uso que le vas a dar y presupuesto tienes buscando en diferentes sitios web y te devolverá los componentes y sus precios correspondientes. 
Metodología:
Para generar la lista de componentes: Utilicé chat-GPT y un prompt bien completo para que busque en la web, filtre los componentes con los mejores precios y mejores prestaciones y devuelva los componentes con una explicación corta en formato de lista para que el usuario pueda leerlo y entenderlo fácilmente.

Para generar la imagen: utilicé un modelo texto-texto(ChatGPT4o-mini) para generar el prompt que luego se lo paso al modelo texto-imagen (Dall-e 2) para un mejor resultado.

Herramientas:Utilizaré VS code, ChatGPT 4o-mini y Dall-E 2

Explicación: Voy a consumirlos por medio de la API de openai instalando en mi entorno openai (pip install openai==0.28) y arriba colocando “import openai”, utilizaré una función para generar la conversación  y otra para generar la imagen en la cual le pasé los atributos por ejemplo (model=”dall-e-2”, size=”1024x1024, n=1).



Implementación:

Prompt 1: Imagina que eres un vendedor de componentes honesto de una tienda de Argentina y un cliente de confianza que no entiende mucho de tecnología busca una PC. Pregúntale únicamente el presupuesto máximo que puede llegar, para que lo va a usar si quiere algo discreto y si necesita periféricos y En base a eso busca componentes acordes a su presupuesto y uso , luego devuelve los precios y especificaciones básicas para que entienda en forma de lista.


Prompt 2: Presupuesto máximo es de $550 000 y la voy a usar para jueguitos y diseño 3D quiero algo llamativo y necesito periféricos.

Prompt 3:Generame un prompt para generar una imagen con todo los componentes y periféricos que mencionaste antes teniendo en cuenta estos aspectos: dar el tamaño aproximado del teclado y del mouse, agrega que el gabinete tiene que tener los vidrios templados opacos , no describas los componentes internos ni la iluminación, no incluyas marcas, sin mucho detalle, indica la cantidad de cada componente, indica que es una imagen de demostración y el formato tiene que ser un párrafo de texto y en inglés.

Prompt 4 (Creado porChatGPT4o-mini): A demonstration image showcasing a complete gaming and 3D design PC setup. The setup includes one black mid-tower case with opaque tempered glass panels, one 24-inch monitor with a slim bezel, one compact mechanical keyboard (approximately 36 cm wide and 13 cm deep), one ergonomic gaming mouse (approximately 13 cm long and 7 cm wide), one set of over-ear gaming headphones with a built-in microphone, one large mousepad, and a pair of stereo speakers. The arrangement is clean and organized, displaying all peripherals alongside the PC case. No internal components or lighting effects are visible.
 



