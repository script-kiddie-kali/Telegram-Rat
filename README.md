# Telegram-Rat
This is a Simple Telegram Rat which utilises Telegram Bot API to act as a C2 server.
To use this Rat for *EDUCATIONAL PURPOSES* only.
1. Create a bot on telegram From BotFather.
2. He will give you the bot's API TOKEN which is important that you *dont share to anyone*
3. Send a message to your bot(A "hi" will work. dont send /start. if /start is only the option then send it and clear the chat history and then send hii)
4. Now after sending the msg go to "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates" Note: Replace the <YOUR_BOT_TOKEN> with your bot's api token.
5. There you will find your chat id like this
6. "chat": {
    "id": -123456789,
    ...
}
7. if chat id is not visible then keep on refreshing the page.
8. Now paste the Bot's API TOKEN and CHAT ID in the python script(i have commented where to put them)
9. Now you can EITHER deploy your pyhton script directly but it wont work if the system doesnt have required libraries 
10. To make sure that Your rat work (in windows) make it an .exe file using pyinstaller(you can search it up on youtube how to convert python files into .exe).

****FEATURES OF THIS RAT****
1. Keylogging ::: It will start Capturing Everything that the user types on their keyload and send the data in a .txt file when the file reaches 1 KB size.<br>
2. Clipboard data Exfiltration (command /clipboard)<br>
***COMMANDS***<br>
   /sysinfo - [provides you with the system information]<br>
   /speech - [make the computer speak]<br>
   /screenshot - [takes a screenshot of the computer screen.]<br>
   /fetch - [provides you with the keylog file. NOTE:the keylogger files is automatically uploaded once the file reaches 1KB]<br>
   /startup - [add the rat to starup so it persists even after reboot]<br>
   /record - [record the screen for a specified duration in seconds]<br>
NOTE: You can type /start or /help to display the above command list.<br>
Further Instructions:<br>
Once running, you can send commands directly through the Telegram bot chat<br>
in the Telegram app itself to control the RAT remotely.<br>
Use commands like /start, /help, /screenshot, etc.<br>
