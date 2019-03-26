import requests
import os

def get_extension_file(name):
    '''Get extension of 'name' file'''
    return name.split('.')[-1]

def download_picture(pic_path, pic_name, pic_dir):
    '''Download picture by 'pic_path' address, 'pic_name' name to 'pic_dir' folder'''
    if not os.path.exists(pic_dir):
        os.makedirs(pic_dir)

    filename = os.path.join(pic_dir, pic_name)
    response = requests.get(pic_path)
    with open(filename, 'wb') as file:
        file.write(response.content)
    return True

def get_Hubble_image_by_id(id):
    '''Download picture with 'id' to 'pic_dir' folder '''

    response = requests.get('http://hubblesite.org/api/v3/image/'+str(id))

    pic_path = response.json()['image_files'][-1]['file_url']
    pic_extension = get_extension_file(pic_path)
    pic_name = "hubble"+str(id)+'.'+pic_extension
    pic_dir = 'images'

    download_picture(pic_path, pic_name, pic_dir)
    return True

def get_Hubble_image_collection(collection):
    '''Get list of Habble telescope picture's id with 'colelction' mark '''

    response = requests.get('http://hubblesite.org/api/v3/images?page=all&collection_name='+collection)
    images_collection = response.json()

    return [images_collection[i]['id'] for i in range(len(images_collection))]

if __name__ == '__main__':
    list_of_pic_id = get_Hubble_image_collection('spacecraft')
    for pic_id in list_of_pic_id:
        get_Hubble_image_by_id(pic_id)
