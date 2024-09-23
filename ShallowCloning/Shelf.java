package ShallowCloning;

class Book implements  Cloneable {
  String title;
  int pages;
  Author author;

  public Book(String title, int pages, Author author) {
    this.title = title;
    this.pages = pages;
    this.author = author;
  }
  public Object clone() throws CloneNotSupportedException {
    return super.clone();
  }
}

class Author {
  String name;
  public Author(String name) {
    this.name = name;
  }
}
public class Shelf {
  public static void main(String[] args) {
    Author author = new Author("John");
    Book book = new Book("Java", 200, author);
    try {
      Book clonedBook = (Book)book.clone();

      clonedBook.author.name = "Jane"; // Affects originalBook.author

      System.out.println(book.author.name); //Jane
    } catch (CloneNotSupportedException e) {
      e.printStackTrace();
    }
  }
}
