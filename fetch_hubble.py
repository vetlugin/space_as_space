import requests
import os
import download_picture as dp

def get_Hubble_image_by_id(id):
    '''Download picture with 'id' to 'pic_dir' folder '''

    response = requests.get('http://hubblesite.org/api/v3/image/{}'.format(id))
    pic_path = response.json()['image_files'][-1]['file_url']
    pic_extension = os.path.splitext(pic_path)[1]
    pic_name = "hubble{}{}".format(id,pic_extension)
    pic_dir = 'images'
    dp.download_picture(pic_path, pic_name, pic_dir)


def get_Hubble_image_collection(collection):
    '''Get list of Habble telescope picture's id with 'colelction' mark '''

    payload = {"page":"all","collection_name":collection}
    response = requests.get('http://hubblesite.org/api/v3/images', params=payload)
    images_collection = response.json()

    return [images_collection[i]['id'] for i in range(len(images_collection))]

if __name__ == '__main__':
    list_of_pic_id = get_Hubble_image_collection('spacecraft')
    print(list_of_pic_id) #отладочный print
    for pic_id in list_of_pic_id:
        get_Hubble_image_by_id(pic_id)
        print (pic_id) #отладочный print
