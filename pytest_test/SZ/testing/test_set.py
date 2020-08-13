# 一个.py文件就是一个模块
def setup_module():
    print("setup_module：模块级别")


def teardown_module():
    print("teardown_module：模块级别")


def setup_function():
    print("setup_function：函数级别")


def teardown_function():
    print("teardown_function：函数级别")


def test_case1():
    print("function--------")


class TestA:
    def setup_class(self):
        print("setup_classA类级别")

    def teardown_class(self):
        print("teardown_classA类级别")

    # setup teardowm 是方法级别的，在每个类里面的测试用例前后分别被调用一次
    def setup(self):
        print("setup：测试用例前的准备")

    def teardown(self):
        print("teardowm：测试用例后的资源释放")

    def test_a(self):
        print("testa")

    def test_b(self):
        print("testb")


class TestB:
    def setup_class(self):
        print("setup_classB类级别")

    def teardown_class(self):
        print("teardown_classB类级别")

    # setup teardowm 是方法级别的，在每个类里面的测试用例前后分别被调用一次
    def setup(self):
        print("setup：测试用例前的准备")

    def teardown(self):
        print("teardowm：测试用例后的资源释放")

    def test_a(self):
        print("testa")

    def test_b(self):
        print("testb")
