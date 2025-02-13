PF Prompt Engineering.
Recicladora Automática

Problema a abordar: Muchas veces las personas no saben donde tirar sus residuos y cómo catalogarlo (cartón, vidrio, plástico,etc).

Solución planteada: La solución planteada es de crear un chatbot al que el usuario le pase la lista de los residuos que quiere tirar y que la IA la clasifique y le devuelva la lista filtrada y ordenada en un excel. Es relevante porque muchas personas en distintos países no saben bien cómo se haría la clasificación de los residuos o cómo podríamos reutilizar los mismos ahí es donde entra el asistente con IA para informar cómo clasificar los residuos o pedirle consejos para saber cómo reutilizarlo y crear algo útil. La IA entraría como el que filtra los desechos y le busca una segunda utilidad a los residuos.


Ejemplo 1:

Usuario: Hola quiero saber como reutilizar estos residuos: papel de regalo, cartón de caja, film, etc.
 
En este caso la IA va a buscar en internet ideas para buscarle una segunda oportunidad.

Ejemplo 2: 
Usuario: Hola me podes indicar donde tirar estos residuos
*lista*

En este caso la IA va a pasarle de nuevo la lista pero ordenada como lata, cartón y papel, vidrio,etc.

Prompts que voy a usar: 
Prompt 1: Saluda al cliente.

Prompt 2: Imagina que eres un separador de residuos y que te pasan la lista de residuos y vos el resultado en el formato que pida el usuario pero filtrada en residuo reciclable que tiene subdivisiones de carton,vidrio,papel y plástico, el residuo orgánico reciclable cascaras de verduras, frutas, semillas, etc y los residuos no reciclables que son curitas, papeles del baño y pañuelos. Sin introduccion ni nada y no respondas hasta que te pasen la lista.Al final de tu respuesta pregunta si quieren que les des consejos de como aprovechar los residuos reciclables solamente si los residuos que te paso son reciclables
.

Prompt 3: Papel de plastico, rollo de carton, botellas PET, botellas de vidrio, restos de comidas, curitas, pilas, botellas de shampoo, desechos de perfumeria, pañuelos, articulos de limpieza, papel de baño, toallitas femininas. Devolvemelo en (formato)


Herramientas a utilizar:

ChatGPT 4o-mini API: Va a ser la IA que clasifique los residuos.

Visual Studio Code: Editor de texto que voy a usar para la programación.

Streamlit:Voy a usarlo para generar el front de mi aplicación.
Instalación de IA: 

Instalar openai en el directorio de trabajo: 
(pip install openai==0.28)
luego incluirlo en el archivo .py 
(import openai)


Demostracion de herramientas descargadas:
ChatGPT: 


OpenAI API key:



Cuenta de streamlit: 

