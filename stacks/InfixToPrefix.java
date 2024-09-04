package stacks;

import java.util.Stack;

class InfixToPrefix {

  public static void main(String[] args) {
    String infix = "(A+B)*C​";
    String prefix = infixToPrefix(infix);
    String postfix = infixToPostfix(infix);
    System.out.println("Infix: " + infix);
    System.out.println("Prefix: " + prefix);
    System.out.println("Postfix: " + postfix);
  }
  

  public static int precedence(char ch) {
    switch (ch) {
      case '+':
      case '-':
        return 1;
      case '*':
      case '/':
        return 2;
      case '^':
        return 3;
    }
    return -1;
  }

  public static String infixToPostfix(String infix){
    Stack<Character> postStack = new Stack<>();
    StringBuilder postfix = new StringBuilder();

    for (char c : infix.toCharArray()) {
      if (Character.isLetterOrDigit(c)){
        postfix.append(c);
      } else if (c == '(') {
        postStack.push(c);
      } else if (c == ')') {
        while (!postStack.isEmpty() && postStack.peek() != '(') {
          postfix.append(postStack.pop());
        }
        postStack.pop();
      } else {
        while (!postStack.isEmpty() && precedence(c) <= precedence(postStack.peek())) {
          postfix.append(postStack.pop());
        }
        postStack.push(c);
      }
    }
    while (!postStack.isEmpty()) {
      postfix.append(postStack.pop());
    }
    return postfix.toString();
  }

  public static String infixToPrefix(String infix){
    // reverse the infix expression
    String reversedInfix = reverseString(infix);

    // replace '(' with ')' and vice versa
    char[] chars = reversedInfix.toCharArray();

    for (int i = 0; i < chars.length ;i++) {
      if (chars[i] == '('){
        chars[i] = ')';
      } else if (chars[i] == ')') {
        chars[i] = '(';
      }
    }
    reversedInfix = new String(chars);

    // convert to postfix

    String reversedPostfix = infixToPostfix(reversedInfix);

    String prefix = reverseString(reversedPostfix);

    return prefix;
  }

  public static String reverseString(String infix) {
    Stack stk = new Stack<>();

    for (char c : infix.toCharArray()) {
      stk.push(c);
    }

    String temp = "";
    while (!stk.empty()) {
      temp+=stk.pop();
    }

    return temp;
  }
}