ops = '><+-.,[]'

def add_diff_to_char(char, diff):
    if char == chr(255) and diff==1:
        return chr(0)
    if char == chr(0) and diff==-1:
        return chr(255)
    return str(unichr(ord(char) + diff))

class BL:
    def __init__(self, code, input, l=[], i=0):
        self.l = l
        self.i = i
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
                try:
                    new_val = add_diff_to_char(self.l[self.i], 1)
                except IndexError:
                    new_val = chr(1)
                if self.i == len(self.l):
                    self.l.append(new_val)
                elif self.i == -1:
                    self.l.insert(0, new_val)
                else:
                    self.l[self.i] = new_val
            elif op == '-':
                # decrement (decrease by one) the byte at the data pointer.
                try:
                    new_val = add_diff_to_char(self.l[self.i], 1)
                except IndexError:
                    new_val = chr(255)
                if self.i == len(self.l):
                    self.l.append(new_val)
                elif self.i == -1:
                    self.l.insert(0, new_val)
                else:
                    self.l[self.i] = new_val
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
                end = BL.find_closing_bracket('['+self.code)
                if end == -1:
                    raise Exception('[ failed to find a matching ]')
                code_to_repeat = self.code[:end]
                self.code = self.code[end+1:]
                while self.l[self.i] != chr(0):
                    bl = BL(code_to_repeat, self.input, self.l, self.i)
                    self.input, res, self.l, self.i = bl.run()
                    self.res.extend(res)
            else:
                raise Exception('unexpected instruction {0}'.format(op))
        return self.input, self.res, self.l, self.i

    @staticmethod
    def find_closing_bracket(code):
        d = process_brackets(code)
        return d[0]-1   # -1 because [ should be excluded

def find_all_char(a_string, a_char):
    return [i for i in range(len(a_string)) if a_string[i]==a_char]

def process_brackets(a_string):
    d = {}
    open_l  = find_all_char(a_string, '[')
    close_l = find_all_char(a_string, ']')
    for close in close_l:
        open = max([open for open in open_l if open < close])
        d[open] = close
        open_l.remove(open)
        # close_l.remove(close)     don't modify what you're iterating over
    return d

def brain_luck(code, input):
    bl = BL(code, input)
    res = bl.run()[1]
    return ''.join(res)

# def brain_luck_recurse(code, input, l, i, res):

if __name__ == '__main__':
    if False:
        # assert add_diff_to_char('C',  1) == 'D'
        # assert add_diff_to_char('C', -1) == 'B'
        #
        # # Echo until byte(255) encountered
        code0 = ',+[-.,+]'
        # # d0 = process_brackets(code0); assert len(d0)==1; assert d0[2]==7
        assert brain_luck(code0, 'Codewars' + chr(255)) == 'Codewars'
        # #
        # # # # Echo until byte(0) encountered
        code1 = ',[.[-],]'
        # # d1 = process_brackets(code1); assert len(d1)==2;
        # # assert d1[1]==7; assert d1[3]==5
        assert brain_luck(code1, 'Codewars' + chr(0)) == 'Codewars'
        # #
        # # # Two numbers multiplier
        # # # print brain_luck(',.', chr(8) + chr(9))
        # # code2 = '[->+>+<<]>>[-<<+>>]'
        # # d2 = process_brackets(code2); assert len(d2)==2;
        # # assert d2[0]==8; assert d2[11]==18
        #
        assert brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)) == chr(72)  #noqa

        x = chr(0)
        for i in range(72):
            x = add_diff_to_char(x, 1)
        print x

    print brain_luck('++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.', '')