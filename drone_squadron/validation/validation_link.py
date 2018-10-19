class ValidationLink:

    def __init__(self, chain, validation):
        self.chain = chain
        self.chain.append(self)
        self.validation = validation

    def next(self):
        location = self.chain.index(self)
        if not self.end():
            return self.chain[location + 1]

    def end(self):
        return self.chain.index(self) + 1 >= len(self.chain)

    def __call__(self, field):
        validation = self.validation(field)
        if not field.is_valid() or self.end():
            return validation
        return self.next()(field)
