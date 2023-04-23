class AD(dict):

    def __init__(self, *args, **kwargs):
        """This initializer simply passes all arguments to dict, so that
        we can create an AD with the same ease with which we can create
        a dict.  There is no need, indeed, to repeat the initializer,
        but we leave it here in case we like to create attributes specific
        of an AD later."""
        super().__init__(*args, **kwargs)

    def __add__(self, other):
        return AD._binary_op(self, other, lambda x, y: x + y, 0)

    def __sub__(self, other):
        return AD._binary_op(self, other, lambda x, y: x - y, 0)

    @staticmethod
    def _binary_op(left, right, op, neutral):
        r = AD()
        l_keys = set(left.keys()) if isinstance(left, dict) else set()
        r_keys = set(right.keys()) if isinstance(right, dict) else set()
        for k in l_keys | r_keys:
            # If the right (or left) element is a dictionary (or an AD),
            # we get the elements from the dictionary; else we use the right
            # or left value itself.  This implements a sort of dictionary
            # broadcasting.
            l_val = left.get(k, neutral) if isinstance(left, dict) else left
            r_val = right.get(k, neutral) if isinstance(right, dict) else right
            r[k] = op(l_val, r_val)
        return r

def ad_max_items(self):
    AD._binary_op(self, other, lambda x, max(x))

AD.max_items = property(ad_max_items)

AD(red=2, green=3, blue=1).max_items
AD(red=2, yellow=3, blue=3, violet=3, pink=1).max_items
