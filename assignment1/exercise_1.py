# import jnettool.tools.elements.NetworkElement
# import jnettool.tools.Routing
# import jnettool.tools.RouteInspector
from test import NetworkElementTest

print "***********************Old Way*******************************"
ne = NetworkElementTest('171.0.2.45')
# ne = jnettool.tools.elements.NetworkElement('171.0.2.45')
try:
    routing_table = ne.getRoutingTable()
except Exception as e:
# except jnettool.tools.elements.MissingVar:
    logging.exception('No routing table found')
    ne.cleanup('rollback')
else:
    num_routes = routing_table.getSize()
    for RToffset in range(num_routes):
        route = routing_table.getRouteByIndex(RToffset)
        name = route.getName()
        ipaddr = route.getIPAddr()
        print "%15s -> %s" % (name, ipaddr)
finally:
    ne.cleanup('commit')
    ne.disconnect()


print "***********************New Way*******************************"

from adapter import NetworkElement
with NetworkElement('171.0.2.45') as ne:
    for route in ne.routing_table:
        print "%15s -> %s" % (route.name, route.ip_addr)
