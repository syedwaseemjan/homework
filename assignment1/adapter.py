# import jnettool.tools.elements.NetworkElement
# import jnettool.tools.Routing
# import jnettool.tools.RouteInspector
from test import NetworkElementTest


class NetworkElementInterface(object):
    def __init__(self, addr):
        raise NotImplementedError()

    @property
    def routing_table(self):
        raise NotImplementedError()


class RouteInterface(object):
    def __init__(self, route):
        raise NotImplementedError()

    @property
    def name(self):
        raise NotImplementedError()

    @property
    def ip_addr(self):
        raise NotImplementedError()


class RoutingTableInterface(object):
    def __init__(self, rt):
        raise NotImplementedError()

    @property
    def num_routes(self):
        raise NotImplementedError()

    def get_route(self, offset):
        raise NotImplementedError()

    def __iter__(self):
        return [self.get_route(x) for x in range(self.num_routes)].__iter__()


class NERoute(RouteInterface):
    def __init__(self, route):
        self.route = route

    @property
    def name(self):
        return self.route.getName()

    @property
    def ip_addr(self):
        return self.route.getIPAddr()


class NERoutingTable(RoutingTableInterface):
    def __init__(self, rt):
        self.rt = rt

    @property
    def num_routes(self):
        return self.rt.getSize()

    def get_route(self, offset):
        return NERoute(self.rt.getRouteByIndex(offset))


class NetworkElement(NetworkElementInterface):
    def __init__(self, addr):
        self.ne = NetworkElementTest(addr)
        #self.ne = jnettool.tools.elements.NetworkElement(addr)
        self._routing_table = None

    @property
    def routing_table(self):
        if not self._routing_table:
            self._routing_table = NERoutingTable(self.ne.getRoutingTable())
        return self._routing_table

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            from traceback import print_exception
            print print_exception(exc_type, exc_val, exc_tb)
            self.ne.cleanup('rollback')
        self.ne.cleanup('commit')
        self.ne.disconnect()

