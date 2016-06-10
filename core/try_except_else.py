try:
    print 'in try'
    raise Exception('an Exception took place')
except Exception, e:
    print 'in except'
else:
    print 'in else'