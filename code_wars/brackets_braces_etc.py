def is_char_open_or_close(caps, char, stack_open_chars):
    index = caps.index(char)
    is_open_char = True if (index%2==0) else False

    # the above if else determines if a char is an open or close char
    # unless if the char is both an open and a close char, for eg - and -
    # we can tell by checking that caps has this char
    # at index as well as at index+1
    # in addition, it's already counted once as open so the 2nd time it should
    # be counted as close
    if index+1<len(caps) \
            and caps[index+1] == char \
            and len(stack_open_chars) > 0 and stack_open_chars[-1] == char:
        is_open_char = False    # the 2 conditions above make it a close char
    return is_open_char

def is_balanced(source, caps):
    stack_open_chars = []
    for c in source:
        if c in caps:
            if is_char_open_or_close(caps, c, stack_open_chars):
                stack_open_chars.append(c)
            else:
                if len(stack_open_chars)==0: return False
                open_char = stack_open_chars.pop()
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
