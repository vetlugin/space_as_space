def download_picture(pic_path, pic_name, pic_dir):
    '''Скачивает картинку с адресом pic_path, с именем pic_name в директорию pic_dir '''
    os.makedirs(pic_dir, exist_ok=True)
    filename = os.path.join(pic_dir, pic_name)
    response = requests.get(pic_path)

    with open(filename, 'wb') as file:
        file.write(response.content)
