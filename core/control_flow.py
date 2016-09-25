# in Java this would not compile but in Python it would

if True:
    x = 3
assert x == 3

# for example
# public class HelloWorld{
#
#      public static void main(String []args){
#         System.out.println("Hello World");
#         int x=3;
#         if (true) {
#             int y=5;
#         }
#         System.out.println(y);
#      }
# }
#
# doesn't compile because y isn't declared in the outer scope
#
# sh-4.3$ javac HelloWorld.java
# HelloWorld.java:9: error: cannot find symbol
#         System.out.println(y);
#                            ^
#   symbol:   variable y
#   location: class HelloWorld
# 1 error

