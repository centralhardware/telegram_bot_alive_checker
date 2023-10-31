## telegram bot alive checker

this is simple web server that allow to send some text to a any telegram chat

environment variable:
- API_ID
- API_HASH
- TELEPHONE - telephone number for account that create api_id/api_hash

web server start on 8088

the body is always `ok`

### usage

make POST request with body 

```json
{
  "username": "username of bot",
  "test": "test"
}
```