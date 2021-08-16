class Book():
  def __init__(self,title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages
   
  def __str__(self):
    return f"{self.title} by {self.author}"
    
  def __len__(self):
    return self.pages
    

book1 = Book('OOPS!','Varun Baba',300)
book2 = Book('Python','Kanetkar',250)

a = input("Do you want book1 or book2?:")

if a == 'book1':
 print(book1)
 print(len(book1))
 
elif a == 'book2':
 print(book2)
 print(len(book2))
 