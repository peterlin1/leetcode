import threading


class Foo(object):
    """
    Suppose we have a class:

    public class Foo {
      public void first() { print("first"); }
      public void second() { print("second"); }
      public void third() { print("third"); }
    }

    The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call
    second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is
    executed after first(), and third() is executed after second().

    Runtime: 64 ms, faster than 74.04% of Python3 online submissions for Print in Order.
    Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Print in Order.

    """

    def __init__(self):
        self.f_e = threading.Event()
        self.s_e = threading.Event()

    def first(self, printFirst):
        """
        Parameters
        ----------
        printFirst : function

        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f_e.set()

    def second(self, printSecond):
        """
        Parameters
        ----------
        printSecond : function

        """

        self.f_e.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.s_e.set()

    def third(self, printThird):
        """

        Parameters
        ----------
        printThird : function

        """

        self.s_e.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
