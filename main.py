class Library:
    def __init__(self):
        self.file = open("books.txt","a+")

        def __del__(self):
            self.file.close()

    def list_books(self):
        self.file.seek(0)
        files=self.file.read()
        files=files.splitlines()
        for file in files:
            file=file.split(',')
            print(f"Book:{file[0]},Author:{file[1]}")

    def add_book(self,name,author,year,page):
        self.file.write(f"{name},{author},{year},{page}\n")
    def remove_book(self,delete):
        self.file.seek(0)
        files = self.file.read()
        new_files=""
        files = files.splitlines()
        for file in files:
            if delete not in file:
                new_files += file + '\n'
        self.file.seek(0)
        self.file.truncate()
        self.file.write(new_files)


lib = Library()

while True:

    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    choice=input("Lütfen istediğiniz seçeneği seçiniz:")
    if choice == "1":
        lib.list_books()
    elif choice == "2":
        book_name=input("Lütfen kitap ismi giriniz:")
        author_name=input("Lütfen kitabın yazarını giriniz:")
        book_year=input("Lütfen kitabın yayınlandığı yılı giriniz:")
        book_page=input("Lütfen sayfa sayısını giriniz:")
        lib.add_book(book_name,author_name,book_year,book_page)
        print("Kitap eklenmiştir")
    elif choice == "3":
        delete=input("Lütfen silmek istediğiniz kitabın ismini yazınız:")
        lib.remove_book(delete)
        print("Kitap silinmiştir")
    elif choice == "q":
        print("program bitmiştir")
        break;
