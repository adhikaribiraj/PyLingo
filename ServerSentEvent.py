import gevent
from gevent.wsgi import WSGIServer

class ServerSentEvent(object):

    def __init__(self, data):
        self.data = data
        self.event = None
        self.id = None
        self.desc_map = {
            self.data : "data",
            self.event : "event",
            self.id : "id"
        }

    def encode(self):
        if not self.data:
            return ""
        #lines = ["%s: %s" % (v, k)
        #         for k, v in self.desc_map.iteritems() if k]
        lines = list()
        for k in self.desc_map:
            if k:
                lines.append("%s: %s" %(self.desc_map[k], k))

        return "%s\n\n" % "\n".join(lines)
