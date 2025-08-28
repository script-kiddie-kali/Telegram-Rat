# Telegram-Rat
This is a Simple Telegram Rat which utilises Telegram Bot API to act as a C2 server.
To use this Rat for *EDUCATIONAL PURPOSES* only.
1. Create a bot on telegram From BotFather.
2. He will give you the bot's API TOKEN which is important that you *dont share to anyone*
3. Send a message to your bot(A "hi" will work. dont send /start. if /start is only the option then send it and clear the chat history and then send hii)
4. Now after sending the msg go to https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates Note: Replace the <YOUR_BOT_TOKEN> with your bot's api token.
5. There you will find your chat id like this
6. "chat": {
    "id": -123456789,
    ...
}
7. if chat id is not visible then keep on refreshing the page.
8. Now paste the Bot's API TOKEN and CHAT ID in the python script(i have commented where to put them)
9. Now you can EITHER deploy your pyhton script directly but it wont work if the system doesnt have required libraries 
10. To make sure that Your rat work (in windows) make it an .exe file using pyinstaller(you can search it up on youtube how to convert python files into .exe)
