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

### GET /memes/{meme_id}
Return current meme
#### Example
```
GET /memes/1
{
    "status": "ok",
    "id": 1,
    "content": "That same feeling"
}
```

### POST /memes
Create new meme with img
##### Headers
Content-Type: multipart/form-data; boundary="sadfjkldsd"
| Name    | Type       | Location | Required |
|---------|------------|----------|----------|
| content | str        | body     | true     |
| img     | image file | body     | true     |

#### Example
```
POST /memes
{
    "status": "ok"
}
```

### PUT /memes/{meme_id}
Edit the meme
##### Headers
Content-Type: multipart/form-data; boundary="sadfjkldsd"
| Name    | Type       | Location | Required |
|---------|------------|----------|----------|
| content | str        | body     | false    |
| img     | image file | body     | false    |

#### Example
```
PUT /memes/1
{
    "status": "ok"
}
```
### DELETE /memes/{meme_id}
Delete the meme
#### Example
```
DELETE /memes/1
{
    "status": "ok"
}
```
### GET /memes/{meme_id}/img
Get img of the meme
### Example
```
GET /memes/1/img
IMAGE FILE
```
