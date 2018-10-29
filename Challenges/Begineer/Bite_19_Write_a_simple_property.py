from datetime import datetime,timedelta

NOW = datetime.now()


class Promo(object):
    
    def __init__(self,name,date):
        
        self.name = name
        self.date = date
        
    @property
    def expired(self):

        
        if self.date < NOW:
            return True
        else:
            return False


def test_promo_not_expired():
    
    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newslet4ter', future_date)
    assert not newsletter_promo.expired

def test_promo_expired():
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    assert twitter_promo.expired
