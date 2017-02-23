def NetworkElementTest(addr):
    ne = lambda: "network element"
    def getRoutingTable():
        rt = lambda: "routing table"
        def getRouteByIndex(offset):
            route = lambda: "route %s" % offset
            def getName():
                return route()
            def getIPAddr():
                return "1.1.1.1"
            route.getName = getName
            route.getIPAddr = getIPAddr
            return route
        rt.getRouteByIndex = getRouteByIndex
        rt.getSize = lambda: 5
        return rt
    ne.getRoutingTable = getRoutingTable
    ne.cleanup = lambda commit_or_rollback: commit_or_rollback
    ne.disconnect = lambda: None
    return ne