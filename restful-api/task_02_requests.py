#!/usr/bin/python3
"""JSONPlaceholder"""

import csv
import requests


def fetch_and_print_posts():
    """Fetch posts from api"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: 200 {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts from api and save to posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        fieldnames = ["id", "title", "body"]

        with open("posts.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

            for post in posts:
                filtered_post = {
                    "id": post.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body"),
                }
                writer.writerow(filtered_post)
