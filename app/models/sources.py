class Sources:
    """
    news class to defina News Objects
    """

    def __init__(self,id,name,author,title,description,publishedAt,Image,url):
        self.id =id
        self.name =name
        self.author = author
        self.title = title
        self.description =description
        self.publishedAt =publishedAt
        self.Image = Image
        self.url = url