import uuid
import requests

def download_picture(width, height, category):
    '''Download random picture from unsplash based on width, height and category.

    :arg width: width of image.
    :arg height: height of image.
    :arg category: category of image.
    '''
    url = f'https://source.unsplash.com/{width}x{height}?{category}'
    r = requests.get(url)

    # First let us check non existing files.
    if r.status_code == 404:
        print('No such file found at %s' % url)
        return
    filename = f'{uuid.uuid4().hex}.jpg'
    with open(filename, 'wb') as fobj:
        fobj.write(r.content)
    print("Download over.")

if __name__ == '__main__':
    width = 500
    height = 500
    category = 'animal'
    download_picture(width, height, category)