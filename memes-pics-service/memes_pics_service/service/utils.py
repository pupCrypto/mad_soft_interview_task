from ..settings import SETTINGS


def gen_img_url(img_name: str) -> str:
    return SETTINGS.ACCESS_ENDPOINT + '/' + img_name
