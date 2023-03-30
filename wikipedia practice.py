import wikipedia
import requests

page = wikipedia.page("beach")

print(page.summary())

print(len(page.images))