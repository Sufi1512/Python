
from instapy import InstaPy
from instapy import smart_run
myusername='sufihere114'
mypassword='khan0000'

session=InstaPy(username= myusername,
                password=mypassword,
                headless_browser=False)
with smart_run(session):
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=1000,
                                    min_followers=100,
                                    min_following=50)
    session.set_do_follow(True,percentage=100)
    #session.set_dont_like(['nsfw','kia','ford'])
    #session.like_by_tags(['bmw','mercedes'],amount=100)
    session.grab_followers(username="__pure_feeling__", amount=10)
