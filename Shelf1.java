class Book implements Cloneable {
  String title;
  int pages;
  Author author;

  public Book(String title, int pages, Author author) {
      this.title = title;
      this.pages = pages;
      this.author = author;
  }

  @Override
  protected Object clone() throws CloneNotSupportedException {
      Book clonedBook = (Book) super.clone();  // Shallow copy of primitives
      clonedBook.author = (Author) author.clone();  // Deep copy of reference field
      return clonedBook;
  }
}

class Author implements Cloneable {
  String name;

  public Author(String name) {
      this.name = name;
  }

  @Override
  protected Object clone() throws CloneNotSupportedException {
      return super.clone();  // Clone the Author object
  }
}

public class Shelf1 {
  public static void main(String[] args) throws CloneNotSupportedException {
      Author author = new Author("John Smith");
      Book originalBook = new Book("Java Programming", 300, author);
      Book clonedBook = (Book) originalBook.clone();  // Deep clone

      clonedBook.author.name = "Jane Doe";  // Does not affect originalBook.author

      System.out.println(originalBook.author.name);  // Output: John Smith
  }
}
