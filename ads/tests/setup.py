from ads.models import Ad

class AdSetup:
    def create_advertisement(self, title='test', author=None, price=1):
        ad = Ad(title=title, description='*'*61, author=author, price=price)
        ad.save()
        return ad
