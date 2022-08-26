class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def find(self, morse):
        if morse == '':  return self.data
        if morse[0] == '.': return self.left.find(morse[1:])
        if morse[0] == '-': return self.right.find(morse[1:])

    def push(self, data, morse):
        # atualiza o no quando a inserção nao for em ordem
        # correta de alimentacao
        # da arvore
        if morse == '' and self.data == '':
            self.data = data
            return

        #  direita
        if morse[0] == '-':
            if self.right is not None:
                self.right.push(data, morse[1:])

            else:
                if len(morse) > 1:
                    self.right = BinaryTree("")
                    self.right.push(data, morse[1:])
                else:
                    self.right = BinaryTree(data)

        # esquerda
        if morse[0] == '.':
            if self.left is not None:
                self.left.push(data, morse[1:])
            else:
                if len(morse) > 1:
                    self.left = BinaryTree("")
                    self.left.push(data, morse[1:])
                else:
                    self.left = BinaryTree(data)

