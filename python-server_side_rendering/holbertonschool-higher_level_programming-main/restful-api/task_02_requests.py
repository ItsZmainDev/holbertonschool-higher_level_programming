#!/usr/bin/python3
"Module to resquest restful api"

import csv
import requests


def fetch_and_print_posts():
    """
    Function to fetch posts from jsonplaceholder and print titles
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Function to fetch posts from jsonplaceholder and save to csv
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        data_to_write = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data_to_write)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
