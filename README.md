# news-platform-api
test project for news-platform-api

# python-Django usage:
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `./manage.py runserver`
- go to `${SITE_URL}/api/overview/` to see all api endpoints
- create POST request to `${SITE_URL}/api/task/` to register 
reset post upvotes task OR do it by shell: `./manage.py shell`,
`from api.tasks import reset_post_upvotes`, `reset_post_upvotes(repeat=24*60*60)`