
import news
import tracker
import weather
import dictionary



def reply_message(msg):
    if(msg=='news updates'):
         return news.news()

    if(msg.split()[0]=='weather'):
        return weather.get_weather(msg.split()[1])

    if(msg.split()[0]=='Weather'):
        return weather.get_weather(msg.split()[1])

    if(msg.split()[0]=='definition'):
        return  dictionary.get_definition(msg.split()[1])

    if(msg.split()[0:2]==['covid','update']):
        return tracker.get_corona_updates(msg.split()[2])

    else:
        return '''Hello, I am a WhatsApp Chatbot made by Vineet Kekatpure,Shreyash Joshi, Sandeep Suhag and Rithik Kalla.\n
                 "To get the most out of me, you can send the following.\n
                 "weather <location>: to get weather updates\n
                 "covid update <country name>: To get latest updates about COVID-19 of the country of your choice\n
                 "definition <term>: To get the definition of the selected term\n
                 "news updates: To get latest News updates\n
                 "Thanks!\n'''