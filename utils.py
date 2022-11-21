from pathlib import Path
import json


bookmarks = Path("data", "bookmarks.json")
comments = Path("data", "comments.json")
posts = Path("data", "posts.json")

def get_all(name = posts):
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except:
        return "not_found"


def get_posts_by_user(user_name, link = posts):
    found_posts = []
    users = []
    for post in get_all(link):
        if post["poster_name"] not in users:
            users.append(post["poster_name"])
        if user_name.lower() == post["poster_name"]:
            found_posts.append(post)
    if user_name.lower() in users:
        return found_posts
    else:
        return "ValueError"


def get_comments_by_post_id(post_id, link = comments, linker = posts):
    found_comments = []
    pk_posts=[]
    for comment in get_all(link):
        if post_id == comment["post_id"]:
            found_comments.append(comment)
    try:
        for post in get_all(linker):
            if post_id == post["pk"]:
                pk_posts.append(post["pk"])
        return found_comments
    except:
        return "ValueError"


def search_for_posts(query, link = posts):
    found_posts = []
    if len(found_posts)<=10:
        for post in get_all(link):
            if query.lower() in post["content"].lower().split(' '):
                found_posts.append(post)
    return found_posts


def get_post_by_pk(pk, link=posts):
    for post in get_all(link):

        if pk == post["pk"]:
            return post
    return []








