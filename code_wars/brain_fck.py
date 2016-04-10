ops = '><+-.,[]'

def add_diff_to_char(char, diff):
    if char == chr(255) and diff==1:
        return chr(0)
    return str(unichr(ord(char) + diff))

class BL:
    def __init__(self, code, input, l=[]):
        self.l = l
        self.i = 0
        self.res = []
        self.code = code
        self.input = input

    def run(self):
        while self.code:
            op = self.code[0]
            self.code = self.code[1:]
            if op == '>':
                # increment the data pointer (to point to the next cell to the right).
                self.i+=1
            elif op == '<':
                # decrement the data pointer (to point to the next cell to the left).
                self.i-=1
            elif op == '+':
                # increment (increase by one) the byte at the data pointer.
                self.l[self.i] = add_diff_to_char(self.l[self.i], 1)
            elif op == '-':
                # decrement (decrease by one) the byte at the data pointer.
                self.l[self.i] = add_diff_to_char(self.l[self.i], -1)
            elif op == '.':
                # output the byte at the data pointer.
                self.res.append(self.l[self.i])
            elif op == ',':
                # accept one byte of input, storing its value in the byte at the data pointer.
                self.l.insert(self.i, self.input[0])
                self.input = self.input[1:]
            elif op == '[':
                # if the byte at the data pointer is zero, then instead of moving
                # the instruction pointer forward to the next command,
                # jump it forward to the command after the matching ] command
                end = self.find_closing_bracket()
                if end == -1:
                    raise Exception('[ failed to find a matching ]')
                code_to_repeat = self.code[:end]
                self.code = self.code[end+1:]
                while self.l[self.i] != chr(0):
                    bl = BL(code_to_repeat, self.input, self.l)
                    self.input, res, self.l = bl.run()
                    self.res.extend(res)
            # elif op == ']':
            #     # if the byte at the data pointer is nonzero, then instead of moving
            #     # the instruction pointer forward to the next command, jump it back
            #     # to the command after the matching [ command.
            #     return code, input, l, i, res
            else:
                raise Exception('unexpected instruction {0}'.format(op))
        return self.input, self.res, self.l

    def find_closing_bracket(self):
        return self.code.rfind(']')


def brain_luck(code, input):
    bl = BL(code, input)
    res = bl.run()[1]
    return ''.join(res)

# def brain_luck_recurse(code, input, l, i, res):

if __name__ == '__main__':
    assert add_diff_to_char('C',  1) == 'D'
    assert add_diff_to_char('C', -1) == 'B'

    # brain_luck('','')
    # Echo until byte(255) encountered
    # print brain_luck(',+[-.,+]', 'Codewars' + chr(255))
    assert brain_luck(',+[-.,+]', 'Codewars' + chr(255)) == 'Codewars'

    # # Echo until byte(0) encountered
    # print brain_luck(',[.[-],]', 'Codewars' + chr(0))
    assert brain_luck(',[.[-],]', 'Codewars' + chr(0)) == 'Codewars'

    # # Two numbers multiplier
    # print brain_luck(',.', chr(8) + chr(9))
    assert brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)) == chr(72)  #noqa

