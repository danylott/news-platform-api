# news-platform-api
test project for news-platform-api

# Docker usage:
- `docker-compose up`

# python-Django usage:
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver`
- go to `${SITE_URL}/api/overview/` to see all api endpoints
- create POST request to `${SITE_URL}/api/task/` to register 
reset post upvotes task OR do it by shell: `./manage.py shell`,
`from api.tasks import reset_post_upvotes`, `reset_post_upvotes(repeat=24*60*60)`
- run in separate terminal: `./manage.py process_tasks`
- (I know that tasks can be done with django celery, but for this MVP 
I use this easier feature)

# API documentation:
- Postman collection documentation: https://documenter.getpostman.com/view/9909300/SzzrZuVT

# Heroku:
- On current moment I cant deploy on heroku - (cant fix error: modulenotfounderror: no module named 'config')
- but everything else - works fine
- I was trying to do it on this app: `evening-savannah-68190`, but 
that exception raised