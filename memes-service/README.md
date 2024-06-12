# How to
## Setup
To setup service to run it locally you need to install poetry
```
python -m venv venv
source venv/bin/activate
pip install poetry
```
Then you need to enter command bellow to install all dependencies
```
poetry install
```
After all instalations you need to migrate all declared models (actually one model) using command bellow. **Be careful, this command is very rude and will drop all your tables in your database**
```
poetry run migration
```
After all of these you can type command bellow to run service. Please check **memes_service/settings.py** to avoid possible errors
```
python run.py
```

## API Docs

### GET /memes
Returns list of memes
| Name  | Type | Location | Default |
|-------|------|----------|---------|
| limit | int  | query    | 10      |
| page  | int  | query    | 0       |

#### Example
```
GET /memes?limit=10&page=0
{
    "status": "ok",
    "memes": [
        {
            "id": 1,
            "content": "That same feeling"
        },
        {
            "id": 2,
            "content": "When you need to express all your humor"
        },
        {
            "id": 3,
            "content": "To be hired in a company"
        }
    ]
}
```

### Get /memes/{meme_id}
Return current meme