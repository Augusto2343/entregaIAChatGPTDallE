
import requests
import openai
import os
from PIL import Image
openai.api_key = "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"

def generarImagen(prompt):
    client_response = openai.Image.create(
        model = "dall-e-3",
        size = "1024x1024",
        prompt=prompt,
        n=1,
        response_format = "url"
    )
    print(client_response.data[0].url)
def obtListadoComponentes ():
    cliente = openai.ChatCompletion.create(
        model = "gpt-4o-mini",
        messages = [
        {
            "role": "user",
            "content": "Imagina que eres un vendedor de componentes honesto de una tienda de Argentina y un cliente de confianza que no entiende mucho de tecnología busca una PC. Pregúntale únicamente el presupuesto máximo que puede llegar, para que lo va a usar si quiere algo discreto y si necesita periféricos y En base a eso busca componentes acordes a su presupuesto y uso , luego devuelve los precios y especificaciones básicas para que entienda."
        }
    ])
    print(cliente.choices[0].message["content"])
    consulta =input("\nEscribí acá tu prompt:")
    cliente = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages = [
            {
                "role":"user",
                "content":consulta
            }]
        )
    print(cliente.choices[0].message["content"])
    cliente = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages = [
            {
                "role": "user",
                "content":"Generame un prompt para generar una imagen con todo los componentes y periféricos que mencionaste antes teniendo en cuenta estos aspectos:  dar el tamaño aproximado del teclado y del mouse, agrega que el gabinete tiene que tener los vidrios templados opacos , no describas los componentes internos ni la iluminacion, no incluyas marcas, sin mucho detalle, indica la cantidad de cada componente, indica que es una imagen de demostracion y el formato tiene que ser un parrafo de texto y en ingles."
            }]
    )
    imagen = cliente.choices[0].message["content"]
    generarImagen(imagen)
obtListadoComponentes()