class mobilephone:
    def call(self):
        print("used for calling")
class smartphone(mobilephone):
    def take_photo(self):
        print("used for taking photo")
ph=smartphone()
ph.call()
ph.take_photo()