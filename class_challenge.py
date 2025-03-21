def class_challenge():
    class Book:
    #books attribute below
        def __init__(self,title,author):
          self.author=author
          self.title=title

    #method
        def read(self):
          return "Reading the Books enriches us with knowledge"

#now objects
    class Encyclopedia(Book):
        pass

    book1=Encyclopedia("Life is Still Beautiful","Enrique Chaij")
    book2=Encyclopedia("Don Quixote","Miguel de Cervantes")
    print(f"First book Details:",book1.title,"by",book1.author)
    print(f"Second book Details:",book2.title,"by",book2.author,)
    print(book2.read(),"\n")

    class story_book(Book):
        def read(self):
            return "story book gives you more vocabulary"
    story1=story_book("Hyena Bills","Nehemy Mbani")
    story2=story_book("Thunderstorm","Wendy Paul")
    print("story Book1 Details:",story1.title,"by",story1.author)
    print("story Book2 Details:",story2.title,"by",story2.author)
    print(story1.read(),"\n")

    class Bible(Book):
        def read(self):
            return "Reading bible purifies our soul and draws us to God"
    bible1=Bible("Genesis","Moses")
    bible2=Bible("Psalms","Daniel")
    print("First Bible book Details:",bible1.title,"by",bible1.author)
    print("Second Bible book Details:",bible2.title,"by",bible2.author)
    print(bible1.read())
#call the function
class_challenge()