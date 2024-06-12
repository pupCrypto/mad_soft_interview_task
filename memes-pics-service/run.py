if __name__ == '__main__':
    import uvicorn
    from memes_pics_service.settings import SETTINGS

    uvicorn.run('memes_pics_service.app:app', host=SETTINGS.HOST, port=SETTINGS.PORT, reload=True)
