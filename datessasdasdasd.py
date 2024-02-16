import datetime

class libraryItem:

    # CONSTRUCTOR
    def __init__(self, t, a, i):
        self.__title = t
        self.__author_artist = a
        self.__itemID = i
        self.__onLoan = False
        self.__dueDate = None
        self.__borrowerID = None

    # GETTER
    def gettitle(self):
        return self.__title
    def getauthor_artist(self):
        return self.__author_artist
    def getitemID(self):
        return self.__itemID
    def getonLoan(self):
        return self.__onLoan
    def getdueDate(self):
        return self.__dueDate

    # SETTER
    def borrowing(self, bi):
        self.__onLoan = True
        self.__dueDate = datetime.datetime.now() + datetime.timedelta(21)
        self.__borrowerID = bi
        borrower.updateitemsOnLoan(1)
    def returning(self):
        self.__onLoad = False
        self.__dueDate = None

    # OTHER
    def printDetails(self):
        print("Title:", self.__title)
        print("Author/Artist:", self.__author_artist)
        print("ItemID:", self.__itemID)
        print("On Loan:", self.__onLoan)
        print("Due Date:", self.__dueDate.strftime("%x"))

class book(libraryItem):

    # CONSTRUCTOR
    def __init__(self, t, a, i):
        libraryItem.__init__(self, t, a, i)
        self.__isRequested = False
        self.__requestedBy = 0
        self.__requestor = []

    # GETTER
    def getisRequested(self):
        return self.__isRequested
    def getrequestedBy(self):
        return self.__requestedBy

    # SETTER
    def request(self):
        self.__isRequested = True
        self.__requestedBy = self.__requestedBy + 1
    def delRequest(self):
        self.__requestedBy = self.__requestedBy - 1
        if self.__requestedBy == 0:
            self.__isRequested = False
        elif self.__requestedBy < 0:
            self.__isRequested = False
            self.__requestedBy = 0

    # OTHER
    def printDetails(self):
        libraryItem.printDetails(self)
        print("Is Requested:", self.__isRequested)
        print("Requested By:", self.__requestedBy)
    
class cd(libraryItem):

    # CONSTRUCTOR
    def __init__(self, t, a, i, g):
        libraryItem.__init__(self, t, a, i)
        self.__genre = g

    # GETTER
    def getgenre(self):
        return self.__genre

    # SETTER
    def setgenre(self, g):
        self.__genre = g

    # OTHER
    def printDetails(self):
        libraryItem.printDetails(self)
        print("Genre:", self.__genre)

class borrower:

    # CONSTRUCTOR
    def __init__(self, n, e, i):
        self.__borrowerName = n
        self.__emailAddress = e
        self.__borrowerID = i
        self.__itemsOnLoan = 0

    # GETTER
    def getborrowerName(self):
        return self.__borrowerName
    def getemailAddress(self):
        return self.__emailAddress
    def getborrowerID(self):
        return self.__borrowerID
    def getitemsOnLoan(self):
        return self.__itemsOnLoan

    # SETTER
    def updateitemsOnLoan(self, n):
        self.__itemsOnLoan = self.__itemsOnLoan + n

    # OTHER
    def printDetails(self):
        print("Borrower Name:", self.__borrowerName)
        print("Email Address:", self.__emailAddress)
        print("Borrower ID:", self.__borrowerID)
        print("Items on Loan:", self.__itemsOnLoan)
