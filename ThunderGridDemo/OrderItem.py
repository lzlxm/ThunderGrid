


class OrderItem:
    def __init__(self):
        self._orderid = ''
        self._goods = ''
        self._destination = ''
        self._delivered = False


    # order id
    @property
    def orderid(self):
        return self._orderid
    @orderid.setter
    def orderid(self, value):
        self._orderid = value


    # goods
    @property
    def goods(self):
        return self._goods
    @goods.setter
    def goods(self, value):
        self._goods = value

    # destination
    @property
    def destination(self):
        return self._destination
    @destination.setter
    def destination(self, value):
        self._destination = value


    # delivered
    @property
    def delivered(self):
        return self._delivered
    @delivered.setter
    def delivered(self, value):
        if value.lower() == 'true':
            self._delivered = True
        else:
            self._delivered = False



