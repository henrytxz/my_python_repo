ops = '><+-.,[]'

def brain_luck(code, input):
    global ops
    l = []
    i = 0   # i for index
    res = []
    brain_luck_recurse(code, input, l, i, res)
    return ''.join(res)

def add_diff_to_char(char, diff):
    if char == chr(255) and diff==1:
        return chr(0)
    return str(unichr(ord(char) + diff))

def brain_luck_recurse(code, input, l, i, res):
    while code:
        op = code[0]
        code = code[1:]
        if op == '>':
            # increment the data pointer (to point to the next cell to the right).
            i+=1
        elif op == '<':
            # decrement the data pointer (to point to the next cell to the left).
            i-=1
        elif op == '+':
            # increment (increase by one) the byte at the data pointer.
            l[i] = add_diff_to_char(l[i], 1)
        elif op == '-':
            # decrement (decrease by one) the byte at the data pointer.
            l[i] = add_diff_to_char(l[i], -1)
        elif op == '.':
            # output the byte at the data pointer.
            res.append(l[i])
        elif op == ',':
            # accept one byte of input, storing its value in the byte at the data pointer.
            l.insert(i, input[0])
            input = input[1:]
        elif op == '[':
            # if the byte at the data pointer is zero, then instead of moving
            # the instruction pointer forward to the next command,
            # jump it forward to the command after the matching ] command
            end = code.rfind(']')
            if end == -1:
                raise Exception('[ failed to find a matching ]')
            code_to_repeat = code[:end]
            while l[i] != chr(0):
                code, input, l, i, res = brain_luck_recurse(code_to_repeat, input, l, i, res)
            return code, input, l, i, res
        # elif op == ']':
        #     # if the byte at the data pointer is nonzero, then instead of moving
        #     # the instruction pointer forward to the next command, jump it back
        #     # to the command after the matching [ command.
        #     return code, input, l, i, res
        else:
            raise Exception('unexpected instruction {0}'.format(op))
    return code, input, l, i, res

if __name__ == '__main__':
    assert add_diff_to_char('C',  1) == 'D'
    assert add_diff_to_char('C', -1) == 'B'

    # brain_luck('','')
    # Echo until byte(255) encountered
    assert brain_luck(',+[-.,+]', 'Codewars' + chr(255)) == 'Codewars'

    # # Echo until byte(0) encountered
    print brain_luck(',[.[-],]', 'Codewars' + chr(0))
    # assert brain_luck(',[.[-],]', 'Codewars' + chr(0)) == 'Codewars'

    # # Two numbers multiplier
    # assert brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)) == chr(72)  #noqa

