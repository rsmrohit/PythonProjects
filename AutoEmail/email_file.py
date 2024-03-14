import yagmail
import pandas
import datetime
from news import NewsFeed 

df = pandas.read_csv('people.csv')
email = yagmail.SMTP(user="rohmam060405@gmail.com", password='aqyrbnpzltilnzck')

def send_email(today, yesterday, row):
    news_feed = NewsFeed(interest=row['interest'], from_date=yesterday.strftime('%Y-%m-%d'), to_date=today.strftime('%Y-%m-%d'), language="en")

    email = yagmail.SMTP(user="rohmam060405@gmail.com", password='aqyrbnpzltilnzck')
    email.send(to=row['email'],
                subject=f"Your {row['interest']} news for today!",
                contents=f"Hi {row['name']}\nSee what's on about {row['interest']} today. \n\n{news_feed.get()}")

if __name__ == "__main__":

    today = datetime.datetime.now()
    yesterday = datetime.datetime.now() - datetime.timedelta(days=2)


    for index, row in df.iterrows():
        send_email(today, yesterday, row)