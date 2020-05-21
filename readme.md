# [u/AAAABOT](https://www.reddit.com/u/AAAABOT/)

I'm doing this because I want to practice deploying web applications that can interact with user input. u/AAAABOT is a reddit bot that replies with a random set of upper and lower case "A"s every time it is pinged. It's running on a ubuntu server using a crontab set to execute every five or so minuets. It adds the url of every reply to a log.txt file which I hope to upgrade to a sql lite database which can be queried by a flask webserver to display on a front end admin page. 

Tools I've used: 

- [Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/)
- [Ubuntu Server](https://ubuntu.com/download/server)
- [Crontab](http://man7.org/linux/man-pages/man8/cron.8.html)

Issues I've come across: 

- Replying to mentions within submissions
- Spamming mod mail
