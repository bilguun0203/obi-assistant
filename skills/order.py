import utils.config as conf

SIZES = ['жижиг', 'дунд', 'том']

QUANTITIES = ['нэг', 'хоёр', 'гурван',
              'дөрвөн', 'таван', 'зургаан', 'долоон', 'найман', 'есөн', 'арван']


class Order:
    def __init__(self, name='пицца', size=SIZES[0], quantity=QUANTITIES[0]):
        self._name = name
        self._size = size
        self._quantity = quantity

    def set_size(self, size=SIZES[0]):
        if size not in SIZES:
            self._size = SIZES[0]
        self._size = size
        return self

    def set_quantity(self, quantity=QUANTITIES[0]):
        quantity = QUANTITIES.index(quantity) + 1
        if quantity < 1:
            self._quantity = 1
        self._quantity = quantity
        return self

    def order(self):
        return '{} ширхэг {} {} амжилттай захиаллаа. Хүргэх хаяг {}'.format(QUANTITIES[self._quantity-1], self._size, self._name, conf.config()['HOME_ADDRESS'])
