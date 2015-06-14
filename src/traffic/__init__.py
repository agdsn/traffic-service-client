from datetime import datetime
import zmq

from messages import common_pb2, replies_pb2, requests_pb2


class Connection(object):
    def __init__(self, uri, context=None):
        self._uri = uri
        if context is None:
            context = zmq.Context()
        self._context = context
        self._socket = self._context.socket(zmq.REQ)
        self._connected = False

    def connect(self):
        assert not self._connected
        self._socket.connect(self._uri)
        self._connected = True

    def disconnect(self):
        assert self._connected
        self._socket.disconnect(self._uri)
        self._connected = False

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, type, value, traceback):
        self.disconnect()

    def send_msg(self, msg):
        assert self._connected
        assert isinstance(msg, requests_pb2.Request)

        self._socket.send(msg.SerializeToString())
        reply = replies_pb2.Reply()
        reply.ParseFromString(self._socket.recv())
        return reply


def get_summary_unix(conn, interval_start, interval_end, clients):
    assert interval_start < interval_end;
    assert len(clients) != 0
    
    request = requests_pb2.Request()
    request.version=1

    message = request.summary
    message.range.start = interval_start
    message.range.end = interval_end

    message.addresses.extend(clients)

    reply = conn.send_msg(request)

    return reply.summary


def get_summary(conn, interval_start, interval_end, clients):
    assert isinstance(interval_start, datetime)
    assert isinstance(interval_end, datetime)

    epoch = datetime(1970,1,1)
    return get_summary_unix(conn,
            int((interval_start - epoch).total_seconds()),
            int((interval_end - epoch).total_seconds()),
            clients)

