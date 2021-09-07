#!/usr/bin/env python3

# IGBoostBot
# InstaAcceleratorBot
import Constants as keys
import Responses as R
import Insta as I
from telegram.ext import *
from telegram import Update
import emoji
import re
import pickle


print("InstaAcceleratorBot has been activated")

#Define functions
IG_POST, IG_LIST, IG_CHECK = range(3)

def start_command(update, context):
    s = open("start.txt", "r")
    update.message.reply_text(emoji.emojize(s.read()))
    s.close()

def help_command(update, context):
    s = open("help.txt", "r")
    update.message.reply_text(emoji.emojize(s.read()))
    s.close()

def handle_message(update, context):
    text = str(update.message.text).lower()  # Receives text from the user
    response = R.sample_responses(text)  # Process the text from the user
    update.message.reply_text(response)  # Replies to the user
####Adding conversation handler

def handle_ig_account(update: Update, context: CallbackContext):
    ''' Entry point of Conversation Handler '''
    update.message.reply_text("Awesome, let's begin! Please, text me your IG account starting with @")
    return IG_POST

def handle_ig_post(update: Update, context: CallbackContext):
    user_message = str(update.message.text).lower()
    check = re.search("^@", user_message)
    if bool(check) == True:
        #save the user Ig account in context pickle file
        context.user_data['igaccount'] = user_message.replace("@","")
        update.message.reply_text("Cool profile! Now please send me the link of the Instagram post you want to accelerate")
        return IG_LIST
    else:
        update.message.reply_text("Sorry, it did not work. Please start over by texting me /accelerate")
        return ConversationHandler.END

def handle_ig_list(update: Update, context: CallbackContext):
    with open('lists', 'rb') as fp:
        ig_links = pickle.load(fp)
        ig_links = list(map(lambda x: x.strip(), ig_links))
        fp.close()

    #f = open("lists.txt", "r")
    #content = f.read()
    #ig_links = content.split("\n")
    #f.close()

    user_message = str(update.message.text)
    check = re.search("https:\/\/www\.instagram\.com\/p\/\w+", user_message)
    if bool(check) == True:
        #save the user's IG post in context pickle file
        context.user_data['igpost'] = user_message
        context.user_data['links'] = ig_links
        tot = len(context.user_data['links'])
        reply_ig_list = '''Perfect! We are almost there\nPlease, comment the following links, then return and text me "done" without airquotes. I will check that you have commented and add your post to the list for the next users\n'''
        update.message.reply_text(reply_ig_list+"\n".join(map(str, context.user_data['links'])))
        update.message.reply_text(str(tot))
        value = context.user_data
        #update.message.reply_text(value)
        return IG_CHECK
    else:
        update.message.reply_text("Sorry, it does not seem to be an Instagram link. Please start over by texting me /accelerate")
        return ConversationHandler.END

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text('The conversation was canceled by you. Text me /accelerate to start again')
    return ConversationHandler.END
#####

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def handle_listcheck(update: Update, context: CallbackContext):
    user_message = str(update.message.text).lower()
    if user_message == "done":
        #Must be a loop for all the list posts
        tot = len(context.user_data['links'])
        good_links = []
        bad_links = []
        for link in context.user_data['links']:
            if I.ig_comment_extract(context.user_data['igaccount'], link) == True:
                good_links.append(link)
            else:
                bad_links.append(link)

        if len(good_links) == tot:
            with open('lists', 'rb+') as fp:
                ig_list2 = pickle.load(fp)
                ig_list2 = list(map(lambda x: x.strip(), ig_list2))
                ig_list2.append(context.user_data['igpost'])
                ig_list2.pop(0)
                fp.seek(0)
                pickle.dump(ig_list2, fp)
                fp.close()

            update.message.reply_text("Awesome! Thank you, your post will be added to the list, so the next users will comment it"+"\n".join(map(str, ig_list2)))
            return ConversationHandler.END
        else:
            reply_ig_list2 = '''Oh oh... I think you might have skipped some. Please, comment the following links and text me again done\n'''
            update.message.reply_text(reply_ig_list2+"\n".join(map(str, bad_links)))
            return IG_CHECK
    else:
        update.message.reply_text('The conversation was canceled by you. Text me /accelerate to start again')
        return ConversationHandler.END

def main():
    pp = PicklePersistence(filename='my_bot')
    updater = Updater(keys.API_KEY, persistence=pp, use_context=True)  # start the bot
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))  # 1st defined function
    dp.add_handler(CommandHandler("help", help_command))  # 2nd defined function

    # Conversation
    # Add conversation handler with the states  IG_POST, IG_LIST
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('accelerate', handle_ig_account)],
        states={
            IG_POST: [MessageHandler(Filters.text, handle_ig_post)],
            IG_LIST: [MessageHandler(Filters.text, handle_ig_list)],
            IG_CHECK: [MessageHandler(Filters.text, handle_listcheck)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dp.add_handler(conv_handler)

    dp.add_handler(MessageHandler(Filters.text, handle_message))  # General conversation

    dp.add_error_handler(error)


    updater.start_polling(5)  # 5 sec the bot waits before checking for new messages
    updater.idle()


main()




