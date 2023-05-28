import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables
from dotenv import load_dotenv   
load_dotenv()                    

bot_id = os.environ.get('bot_id')
api_key = os.environ.get('api_key')


bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello','hi'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello! Welcome to cinebot that will show movie information for you and export it in a CSV file.\n\n')
   
@bot.message_handler(commands=['stop', 'bye','tata'])
def goodbye(message):
    
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
   


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Kashmir Files\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

# TODO: 1.2 Get movie information from the API
    
@bot.message_handler(func=lambda message: botRunning, commands=['movie','film'])
def getMovie(message):

    temp = message.text.split(' ')
    teleid = f"https://api.telegram.org/bot{bot_id}"
    name = ''
    for a in temp:
        if a !='/movie':
            name = name + a + ' '
    bot.reply_to(message,'Please Wait...')
    response = requests.get(f'http://www.omdbapi.com/?t={name}&apikey={api_key}')


    json_file = response.json()
    base_url = f"{teleid}/sendPhoto"

    # TODO: 1.3 Show the movie information in the chat window
    if json_file['Response'] == 'False':
        bot.reply_to(message,'Movie not found!,Please try again')
    else:
        bot.send_message(message.chat.id,"Movie found!")
        parameters = {
        "chat_id" : f'{message.chat.id}',
        "photo" : json_file['Poster'],
        "caption" : f"Title = {json_file['Title']}\nYear= {json_file['Year']}\nReleased = {json_file['Released']}\nIMDb Rating= {json_file['imdbRating']}"
        }

    resp = requests.get(base_url, data = parameters)
    print(resp.text)
    print(response.json())

    # TODO: 2.1 Create a CSV file and dump the movie information in it
    with open(f'movies{message.chat.id}.csv', 'a') as csvfile:
        name_list =['Title','Year','Released','IMDb Rating' ]
        impo = csv.DictWriter(csvfile, fieldnames = name_list)
        if os.path.getsize(f'movies{message.chat.id}.csv') == 0:
            impo.writeheader()
        impo.writerow({'Title':json_file['Title'],'Year':json_file['Year'],'Released':json_file['Released'],'IMDb Rating':json_file['imdbRating']})
   
 #TODO: 2.2 Send downlodable CSV file to telegram
@bot.message_handler(func=lambda message: botRunning, commands=['export','csv'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    files ={'document':open(f'movies{message.chat.id}.csv','rb')}
    resp = requests.post(f"https://api.telegram.org/bot{bot_id}/sendDocument?chat_id={message.chat.id}",files=files)


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
   
bot.infinity_polling()