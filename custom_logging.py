import logging

logging.TRACE = logging.DEBUG - 1
logging.addLevelName(logging.TRACE, 'TRACE')

def trace(self, message, *args, **kws):
    self.log(logging.TRACE, message, *args, **kws)
logging.Logger.trace = trace

logging.basicConfig()
l = logging.getLogger('test_logger')
l.setLevel('TRACE')
l.trace('test')
