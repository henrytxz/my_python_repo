def is_char_open_or_close(caps, char, stack_open_chars):
    #print 'caps: {0}'.format(caps)
    #print 'char: {0}'.format(char)
    index = caps.index(char)
    #print 'index is {0}'.format(index)
    #is_open_char = True
    is_open_char = True if (index%2==0) else False
    #print is_open_char

    # char is both an open and a close char, for eg - and -
    if caps[index+1] == char and stack_open_chars[-1] == char:
        is_open_char = False    # the 2 conditions above make it a close char
    return is_open_char

#def is_close_char(caps, char):
#    return caps.index(char)%2==1

def is_balanced(source, caps):
    stack_open_chars = []
    for c in source:
        if c in caps:
            if is_char_open_or_close(caps, c, stack_open_chars):
                stack_open_chars.append(c)
            else:
                if len(stack_open_chars)==0: return False
                open_char = stack_open_chars.pop()
                #print caps.index(c)
                #print caps.index(open_char)
                if not (caps.index(c) == caps.index(open_char)+1):
                    if c != open_char:
                        return False

    return True if len(stack_open_chars)==0 else False

class Validate(object):
  @staticmethod
  def assert_equals(x, y):
      assert x==y
    # try:
    #     assert x==y
    # except:
    #     print 'assert failed'
    #     print 'Produced:'
    #     print_list_of_lists(x)
    #     print 'Expected:'
    #     print_list_of_lists(y)
    #     print '='*88

if __name__ == '__main__':
    caps = '()[]'
    assert is_char_open_or_close(caps, '(', []) == True
    assert is_char_open_or_close(caps, '[', []) == True
    assert is_char_open_or_close(caps, ']', []) == False
    assert is_char_open_or_close(caps, ')', []) == False

    Validate.assert_equals(is_balanced("(Sensei says yes!)", "()"), True)
    Validate.assert_equals(is_balanced("(Sensei says no!", "()"), False)

    Validate.assert_equals(is_balanced("(Sensei [says] yes!)", "()[]"), True)
    Validate.assert_equals(is_balanced("(Sensei [says) no!]", "()[]"), False)

    Validate.assert_equals(is_balanced("Sensei says -yes-!", "--"), True)
    Validate.assert_equals(is_balanced("Sensei -says no!", "--"), False)
