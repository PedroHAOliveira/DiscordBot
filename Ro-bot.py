import discord
import asyncio
import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

print(f"Chave API do Gemini: {GEMINI_API_KEY}")  # Depuração

# Configurar intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

usuarios_especificos = ["kynoa"]

# Lista de IDs dos canais onde a mensagem será enviada
"""CANAL_IDS = [
    1342217517900496947,  # Primeiro canal
    763290122720378880  # Segundo canal
]"""


# Função para chamar a API do Gemini
def get_gemini_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except requests.exceptions.RequestException as e:
        return f"Erro ao chamar a API do Gemini: {e}"


@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

    # Iterar sobre os IDs dos canais e enviar a mensagem
    for canal_id in CANAL_IDS:
        channel = client.get_channel(canal_id)
        if channel:
            await channel.send("Olá! O Ro-Bot acabou de ser iniciado. Estou pronto para ajudar!")
            print(f"Mensagem enviada ao canal {channel.name} (ID: {canal_id})")
        else:
            print(f"Erro: Canal com ID {canal_id} não encontrado.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("Pong!")
        return

    if message.content.lower().startswith(("olá", "ola", "olá!", "ola!", "olaa")):
        if str(message.author) in usuarios_especificos:
            await message.channel.send(f"Olá {str(message.author).title()}!")
        elif str(message.author) == "anajcs0431":
            await message.channel.send('Oi gatinha! Tá solteira?😘')
        else:
            await message.channel.send("Olá, sou o Ro-Bot!")
        return

    if message.content.lower().startswith("cade"):
        await message.channel.send("Cadeeeeee?")
        await asyncio.sleep(1)
        await message.channel.send("Mostra as plays!")
        return

    if str(message.channel) == "📷・fotos・📷" and message.content != "":
        await message.channel.purge(limit=1)
        return

    if message.content.startswith("!ro"):
        prompt = message.content[len("!ro"):].strip()
        if prompt:
            response = get_gemini_response(prompt)
            await message.channel.send(response)
        else:
            await message.channel.send("Digite algo após '!ro'!")
        return


client.run(DISCORD_TOKEN)