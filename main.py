import requests
import os
from fastapi import FastAPI
from dotenv import load_dotenv

# TODO
# 1. Criar uma API simples que retorna um valor estático ao ser chamado.
# 2. Criar uma rota que recebe um local e retorna os dados do clima desse local.

load_dotenv()
api_url = os.getenv("API_URL")
api_key = os.getenv("API_KEY")


app = FastAPI()

#Rotas
@app.get("/")
def show_instructions():
    json_response = {
        "instruction": "To get the weather data, use the endpoint /weather/{location}",
        "EXAMPLES": [
            "/New York, NY, Estados Unidos",
            "/Q2MM+2Q Nova Iorque, Nova York, EUA",
            "/1000 5th Ave, New York, NY 10028, Estados Unidos"
            "/Trumpington St, Cambridge CB2 1RB, Reino Unido",
            "/Av. Pedro Álvares Cabral - Vila Mariana, São Paulo - SP, 04094-050",
            "/Rua Araribá, 430 - Concórdia, Belo Horizonte - MG, 31210-700",
        ],
        "environment_variables": {
            "API_URL": api_url,
            "API_KEY": api_key
        }
    }
    print("API_URL:", api_url)
    print("API_KEY:", api_key)
    return json_response

@app.get("/{location}")
def fetch_weather(location: str):
    url = api_url + location + api_key
    
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    pass