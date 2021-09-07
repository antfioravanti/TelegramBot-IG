# TelegramBot-IG
 A Telegram bot used to increase the engagment rate of the users by crowdsourcing comments from other users.
 
 ### How it works
 1. Text */accelerate* to the bot to initiate the conversation
 2. Provide the Instagram profile starting with the @ handle.
 3. Provide the link of the Instagram post that the bot should save.
 4. A list of other Instagram links is returned. These are links of previous people that have used the bot. The user should log-in with the provided Instagram account and comment each of the provided posts.
 5. When finished, text */done*
 6. The bot verifies that the user has commented all the provided links by connecting to the Instagram API
 7. If all links have been commented, then the bot saves the provided link to the list and will provide it to the next user.
