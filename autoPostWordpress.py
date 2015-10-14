# AWBL - Automatic Wordpress Build Log
# Created by Ryan McCartney
# ryanmccart.me 

# MIT LICENCE

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from datetime import datetime
import time, subprocess, os

bashCommand = "Autogitlog.sh"
os.system(bashCommand)
time.sleep(3)
    
def loadFile():

    global lines
    lines = [line.rstrip('\n') for line in open('log.txt')]
    
    global title
    title = lines[4]
    
    global description
    description = lines[6]

def posting():

    wp = Client('<YOURWORDPRESSSIT>/xmlrpc.php','YOURUSERNAME','YOURPASSWORD')
    #publish_date = (publish, '%a %b %d %H:%M:%S %Y %z')

    post = WordPressPost()
    post.title = title #Commit Title
    post.content = description #Commit message
    post.post_status = 'publish'
    post.terms_names = {
        'category': ['12SDD']
        }
    #post.date = publish_date

    #Creates a new wordpress post and posts it on the site.
    wp.call(NewPost(post))

#setDateFile()
loadFile()
posting()


#----------------------------------

def setDateFile():
    f = open("log.txt")
    lines = f.readlines()
    f.close()
    f = open("datelog.txt","w")

    for line in lines:
        if line.startswith('Date:'):
            f.write(line[8:32])
    f.close()

    publishline = [line.rstrip('\n') for line in open('datelog.txt')]
    pub = str(publishline[:24])
    print(pub)
