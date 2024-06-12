from ..settings import SETTINGS


def get_pic_upload_url():
    return 'http://' + SETTINGS.IMG_SERVICE_HOST + '/upload'
