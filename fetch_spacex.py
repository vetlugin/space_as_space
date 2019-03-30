import requests
import os
import download_picture as dp

def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')
    list_of_pic = response.json()['links']['flickr_images']

    for pic_number, pic in enumerate(list_of_pic):
        dp.download_picture(pic, 'spacex{}.jpg'.format(pic_number), 'images')

if __name__ == '__main__':
    fetch_spacex_last_launch()
