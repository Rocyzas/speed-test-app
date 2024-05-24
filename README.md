# Speed Test App

## Development setup

### Backend setup
`pip install -r requirements.txt`  
run as `python app.py`  
run tests `pytest test_routes.py `

Session is stored on server side. For that install redis  
run redis (macOS) - `brew services start redis` (verify if running with `redis-cli ping`)

(locally redis conf at /opt/homebrew/etc/redis.conf)

### Frontend setup
`npm install`  
run as `npm start`  



------------------------------------------------

Todo:
- On restart keep session same
- Set timer during which user is allowed to submit code
- Return %
- Unit tests