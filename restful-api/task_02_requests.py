#!/usr/bin/python3
"""JSONPlaceholder"""

import csv
import requests


def fetch_and_print_posts():
    """Fetch and print"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.statuse_code))
    if response.statuse_code == 200:
        posts = response.json()

        fieldname = ["id", "title", "body"]

        with open("posts.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldname=fieldname)

            writer.writeheader()

            for post in posts:
                filtered_post = {
                    "id": posts.get("id"),
                    "title": post.get("title"),
                    "body": post.get("body"),
                }
                writer.writerow(filtered_post)
