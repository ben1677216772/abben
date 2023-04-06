import discord
import openai
openai.api_key = 'token from openai'
TOKEN = 'token from discord'
intents = discord.Intents.default()
intents.message_content = True
intents.members =True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} connected')
    
@bot.event
async def on_message(message):
    if message.content.startswith('!คำถาม'):
        question=message.content[7:]
        await message.channel.send('กำลังประมวลผล...')
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": str(question)}
            ])
        answer = response.choices[0].message.content
        await message.channel.send(str(answer))
        
        
bot.run(TOKEN)
