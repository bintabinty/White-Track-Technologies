class camera:
    def take_photo(self):
        print("used for taking stills")
class phone:
    def call(self):
        print("used for calling")
class smartphone(camera,phone):
    def take_video(self):
        print("used for taking videos")
obj=smartphone()
obj.call()
obj.take_photo()
obj.take_video()