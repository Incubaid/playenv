from JumpScale import j

import telebot
from telebot import types

bot = telebot.TeleBot("187850192:AAHwllKfX4BaSo_CHDZAvcMfZcEF4mVtvXM")

# info see
# https://github.com/eternnoir/pyTelegramBotAPI

#to install lib:
#pip3 install pyTelegramBotAPI

#THIS IS FOR BOT @gigplaybot
#search for it to play


##DOWNLOAD SOME EXAMPLE FILES WHICH CAN BE USED 


AUDIOFILE = "https://ia802508.us.archive.org/5/items/testmp3testfile/mpthreetest.mp3"
STICKERFILE = "https://telegram-stickers.github.io/public/stickers/flags/8.png"
url="http://www.greenitglobe.com/en/images/logo.png"
image = "%s/giglogo.png"%j.dirs.tmpDir
sound = "%s/test.mp3"%j.dirs.tmpDir
sticker = "%s/sticker.png"%j.dirs.tmpDir
#j.sal.nettools.download(url,image,overwrite=False)
#j.sal.nettools.download(AUDIOFILE,sound,overwrite=False)
#j.sal.nettools.download(STICKERFILE,sticker,overwrite=False)


#EASY EXAMPLES
###############


# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
    pass


# #Which could also be defined as:
# def test_message(message):
#     return message.document.mime_type == 'text/plan'

# @bot.message_handler(func=test_message, content_types=['document'])
# def handle_text_doc(message):
#     pass

@bot.message_handler(commands=['pic'])
def send_picture(message):    
    image2=open(image,'rb')
    bot.send_photo(message.chat.id,image2)


@bot.message_handler(commands=['sound'])
def send_sound(message):    
    obj=open(sound,'rb')
    bot.send_audio(message.chat.id,obj)

@bot.message_handler(commands=['sticker'])
def send_sound(message):    
    obj=open(sticker,'rb')
    bot.send_sticker(message.chat.id,obj)

@bot.message_handler(commands=['location'])
def send_location(message):    
    lat=25.15
    lon=55.18
    bot.send_location(message.chat.id, lat, lon)


@bot.message_handler(commands=['start'])
def send_welcome(message):    
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['virtualdc'])
def send_welcome(message):    
    msg = bot.reply_to(message, "Howdy, how are you doing? Let's define a virtual datacenter! what is the name of you virtual datacenter?")
    bot.register_next_step_handler(msg, process_name_cloudspace)


#EXAMPLE HOW TO ASK MULTIPLE QUESTIONS
#######################################

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None

    def __repr__(self):
        return str(self.__dict__)

class Virtualmachine:
    def __init__(vm, vdcname):
        vm.vm = None
        vm.cloudspace = vdcname
        vm.os = None
        vm.cores = None
        vm.memory = None

    def __repr__(vm):
        return str(vm,__dict__)

# This section handles the VM questionaire
def process_name_cloudspace(message):
    try:
        chat_id = message.chat.id
        vdcname = message.text
        vm = Virtualmachine(vdcname)
        user_dict[chat_id] = vm
        msg = bot.reply_to(message, 'What is the Virtual Machine name?')
        bot.register_next_step_handler(msg, process_name_vm)
    except Exception as e:
        bot.reply_to(message, "ooops")

def process_name_vm(message):
    try:
        chat_id = message.chat.id
        vname = message.text
        vm = user_dict[chat_id]
        vm.vm = vname


        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('1core', '2cores', '4cores', '8 cores', '16 cores')
        msg = bot.reply_to(message, 'What is the number of cores that your VM needs?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_core_step)
    except Exception as e:
        bot.reply_to(message, "ooops")


def process_core_step(message):
    try:
        chat_id = message.chat.id
        cores = message.text
        vm = user_dict[chat_id]
        vm.cores = cores

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('1GB', '2GB', '4GB', '8GB', '16GB')
        msg = bot.reply_to(message, 'What is the szie of memory that your VM needs?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_memory_step)
    except Exception as e:
        bot.reply_to(message, "ooops")

def process_memory_step(message):
    try:
            chat_id = message.chat.id
            memory = message.text
            vm = user_dict[chat_id]
            vm.memory = memory

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('Ubuntu-15.10', 'Ubuntu-14.20', 'Windows', 'RouterOS')
            msg = bot.reply_to(message, 'What Operating System do you require?', reply_markup=markup)
            bot.register_next_step_handler(msg, process_os_step)
    except Exception as e:
        bot.reply_to(message, "ooooops")

def process_os_step(message):
    try:
            chat_id = message.chat.id
            os = message.text
            vm = user_dict[chat_id]
            vm.os = os

            bot.send_message(chat_id, 'Thank you for this information, I will no go and deploy a machine:\n Machine name: ' + vm.vm + '\n Operating system:' + vm.os + '\n Nr. of Cores:' + vm.cores + '\n Nr. of GB memory:' + vm.memory)
    except Exception as e:
        bot.reply_to(message, "ooooops")

# This section handles the /questions section
@bot.message_handler(commands=['questions'])
def send_askname(message):
    msg = bot.reply_to(message, """\
What's your name?
""")
    bot.register_next_step_handler(msg, process_name_step)



def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'How old are you?')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')



def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Age should be a number. How old are you?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Male', 'Female')
        msg = bot.reply_to(message, 'What is your gender.', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Male') or (sex == u'Female'):
            user.sex = sex
        else:
            msg = bot.reply_to(message, "ERROR IN INPUT: please specify Male or Female.")
            return bot.register_next_step_handler(msg, process_sex_step)
        bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
    except Exception as e:
        bot.reply_to(message, 'oooops')


#DEBUG
#######################################
#@bot.message_handler(commands=['debug'])
#def process_debug(message):
#
#    user=user_dict[message.chat.id]
#
#    msg="DEBUG NOW debug, go to console of bot"
#    print (msg)
#    bot.reply_to(message,msg)
#
#    from IPython import embed
#    embed()



#MAIN
################

bot.polling()


"""
in botfather do

/setcommands

and then paste

questions - answer some questions
pic - show image
sticker - show sticker
sound - audio
location - show dubai location
debug - go into ipshell in telegram robot on server

"""