#Credentials:
import instaloader
import re
import Constants as keys
L = instaloader.Instaloader() #initialize instaloader
USER = keys.USER
PASSWORD = keys.PASSWORD
L.login(USER, PASSWORD)

def ig_comment_extract(username,postlink):
    shortcode = re.findall(r"(?<=\/p\/)(.*?)(?=\/)", postlink)[0]
    post = Post.from_shortcode(L.context, shortcode)
    comments = post.get_comments()
    users = []
    for comment in comments:
        users.append(str(comment.owner.username))

    return True if username in users else False
