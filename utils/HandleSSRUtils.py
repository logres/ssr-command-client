'''
@Author: tyrantlucifer
@E-mail: tyrantlucifer@gmail.com
@Date: 2020/12/7 下午16:08
'''

import sys
import signal
sys.path.append('../')
from shadowsocks import daemon, eventloop, tcprelay, udprelay, asyncdns
from logger.Logging import *

class ControlSSR(object):

    def __init__(self):
        pass

    def start(self, ssrDict, *args):
        ssrDict['local_address'] = args[0]
        ssrDict['local_port'] = args[1]
        ssrDict['timeout'] = args[2]
        ssrDict['workers'] = args[3]
        if not ssrDict.get('dns_ipv6', False):
            asyncdns.IPV6_CONNECTION_SUPPORT = False
        daemon.daemon_exec(ssrDict)
        try:
            dns_resolver = asyncdns.DNSResolver()
            tcp_server = tcprelay.TCPRelay(ssrDict, dns_resolver, True)
            udp_server = udprelay.UDPRelay(ssrDict, dns_resolver, True)
            loop = eventloop.EventLoop()
            dns_resolver.add_to_loop(loop)
            tcp_server.add_to_loop(loop)
            udp_server.add_to_loop(loop)

            def handler(signum, _):
                logging.info('received SIGQUIT, doing graceful shutting down..')
                tcp_server.close(next_tick=True)
                udp_server.close(next_tick=True)

            signal.signal(getattr(signal, 'SIGQUIT', signal.SIGTERM), handler)

            def int_handler(signum, _):
                logger.info("ShadowsocksR is stop")
                sys.exit(1)

            signal.signal(signal.SIGINT, int_handler)
            daemon.set_user(ssrDict.get('user', None))
            logger.info('ShadowsocksR is start on {0}:{1}'.
                        format(args[0], args[1]))
            loop.run()
        except Exception as e:
            logger.error(e)
            sys.exit(1)