import threading


class FooBar(object):
    """
    Suppose you are given the following code:

    class FooBar {
      public void foo() {
        for (int i = 0; i < n; i++) {
          print("foo");
        }
      }

      public void bar() {
        for (int i = 0; i < n; i++) {
          print("bar");
        }
      }
    }

    The same instance of FooBar will be passed to two different threads. Thread A will call foo() while thread B will
    call bar(). Modify the given program to output "foobar" n times.

    Runtime: 76 ms, faster than 78.05% of Python3 online submissions for Print FooBar Alternately.
    Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Print FooBar Alternately.

    """

    def __init__(self, n):
        self.n = n
        self.foo_e = threading.Event()
        self.bar_e = threading.Event()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            if i > 0:
                self.bar_e.wait()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_e.clear()
            self.foo_e.set()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.foo_e.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_e.clear()
            self.bar_e.set()
