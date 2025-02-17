class ProductOfNumbers:

    def __init__(self):
        self._prefix_product = [1]

    def add(self, num: int) -> None:
        if not num:  # if num is 0, reset prefix product
            self._prefix_product = [1]
        else:
            self._prefix_product.append(self._prefix_product[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self._prefix_product):
            return 0
        return self._prefix_product[-1] // self._prefix_product[-1 - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
