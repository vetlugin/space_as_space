import requests
import os

def download_picture(pic_path, pic_name, pic_dir):
    '''Скачивает картинку с адресом pic_path, с именем pic_name в директорию pic_dir '''
    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)

    filename = os.path.join(pic_dir, pic_name)

    response = requests.get(pic_path)

    with open(filename, 'wb') as file:
        file.write(response.content)
    return True

def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')

    list_of_pic = response.json()['links']['flickr_images']

    for pic_number, pic in enumerate(list_of_pic):
        download_picture(pic, 'spacex{}.jpg'.format(pic_number), 'images')
    return True

if __name__ == '__main__':
    fetch_spacex_last_launch()
