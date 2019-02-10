Transfer bot

This bot pulls messages from telegram channel and sends it into the slack channel.

!!!! IMPORTANT !!!!
  This app is not deployed. To run it you should deploy or run through a tunnel. Also write your telegram and slack tokens in telegram_stuff/settings.py
  
How it works?
  
  1) Create telegram channel and add bot there (or add it in existing channel).
  2) Write message in this channel in correct format: /add_link <your link on slack channel>
  Example: /add_link https://workspace.slack.com/messages/XXXXXXXXX/
  This command will add your slack channel id in redis db.
  Don`t worry. This message will not make a mess in telegram channel because the message will be deleted immediately.
  3) Add slack bot in your slack workspace.
  4) That`s all. The next posts will be sent in your slack automatically. 

If you will have some questions/ideas, write on that email: stanish2000@gmail.com
