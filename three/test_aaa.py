class TestAdd:
    def add(self, a, b):
        return a + b    

    def test_int(self):
        res = self.add(a=1, b=2)
        assert res == 3

    def test_str(self):
        res = self.add(a="1", b="2")
        assert res == "12"

    def test_list(self):
        res = self.add(a=[1], b=[2])
        assert res == [1, 2]