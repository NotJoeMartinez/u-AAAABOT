import praw, random, string, re, time
import config as cf 
from datetime import datetime

now = datetime.now()

def randomAString():
    letters = 'Aa'
    return ''.join(random.choice(letters) for i in range(random.randint(20,40)))
    

reddit = praw.Reddit(client_id=cf.abot_id,
                     client_secret=cf.abot_client_secret,
                     user_agent=cf.abot_user_agent,
                     username=cf.abot_uname,
                     password=cf.abot_password)


print(reddit.user.me())

def run_bot():
    # read new inbox messages 
        # reply to to item 
        try: 
            for item in reddit.inbox.unread(limit=None):
            # replies to inbox mention with the output of randomAString() 
                item.reply(randomAString())
                item.mark_read()
                print("replied to comment {} ".format(str(item)))
                # This opens a file a write the url to the metion in it's inbox, along with the datetime 
                with open("log.txt","a") as file:
                    file.write("\n" + str(item) + ' ' +  'https://www.reddit.com'+ item.parent().permalink + str(item) + ' ' + str(now))

               
        # Catches rate limit 
        except praw.exceptions.RedditAPIException as e: 
            print(e)
            if (e.error_type == "RATELIMIT"):
                delay = re.search("(\d+) minutes", e.message)

                if delay:
                    delay_seconds = float(int(delay.group(1)) * 60)
                    print("rate limit speeping: {mins} mins".format(mins = delay_seconds))
                    time.sleep(delay_seconds)
                else:
                    delay = re.search("(\d+ seconds", e.message)
                    delay_seconds = float(delay.group(1))
                    print("rate limit speeping: {secs} secs".format(secs = delay_seconds))
                    time.sleep(delay_seconds)
        finally: 
            print("We've run out of comments or something broke")
            return 

run_bot()

                
    



    
