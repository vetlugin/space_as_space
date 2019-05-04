import requests
import os
import download_picture as dp
import datetime


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')
    list_of_pic = response.json()['links']['flickr_images']
    mission_name = response.json()['mission_name']
    mission_patch_path = response.json()['links']['mission_patch']

    dp.download_picture(mission_patch_path, f'spacex{mission_name}-mission_patch.jpg', 'images')
    for pic_number, pic in enumerate(list_of_pic):
        dp.download_picture(pic, f'spacex{mission_name}-{pic_number}.jpg', 'images')

if __name__ == '__main__':
    fetch_spacex_last_launch()
