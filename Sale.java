interface Product {
  void printAmount(double price, int qty);
}
public class Sale {
  static Product p = new Product() {
    @Override
    public void printAmount(double price, int qty) {
      int sold = (int)price * qty;
      System.out.println(sold);
    }
  };

  public static void main(String[] args) {
    p.printAmount(11.8, 2);
  }
}
