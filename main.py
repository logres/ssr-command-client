'''
@Author: tyrantlucifer
@E-mail: tyrantlucifer@gmail.com
@Date: 2020/12/8 下午14:20
'''

import argparse
from funcitions.Functions import *

u = Update()
d = Display()
h = Hanlder()

def get_parser():
    parser = argparse.ArgumentParser(description="The ssr command client based Python.")
    parser.add_argument("-l", "--list", action="store_true", help="show ssr list")
    parser.add_argument("-p", "--port", default=1080, metavar="local_port", type=int, help="assign local proxy port,use with -c or --fast-node")
    parser.add_argument("-s", "--start", metavar="ssr_id", type=int,help="start ssr proxy")
    parser.add_argument("-S", "--stop", default=0, metavar="ssr_id", type=int, help="stop ssr proxy")
    parser.add_argument("-u", "--update", action="store_true", help="update ssr list")
    parser.add_argument("-c", "--config", metavar="ssr_node_id", type=int, help="generate ssr config json")
    parser.add_argument("-v", "--version", action="store_true", help="display version")
    parser.add_argument("--test-speed", action="store_true", help="test ssr nodes download and upload speed")
    parser.add_argument("--fast-node", action="store_true", help="generate fast ssr config json")
    parser.add_argument("--setting-url", metavar="ssr_subscribe_url", help="setting ssr subscribe url")
    parser.add_argument("--setting-address", metavar="ssr_local_address", help="setting ssr local address")
    parser.add_argument("--list-url", action="store_true", help="list ssr subscribe url")
    parser.add_argument("--add-url", metavar="ssr_subscribe_url", help="add ssr subscribe url")
    parser.add_argument("--remove-url", metavar="ssr_subscribe_url", help="remove ssr subscribe url")
    parser.add_argument("--list-address", action="store_true", help="list ssr local address")
    parser.add_argument("--parse-url", metavar="ssr_url", help="pares ssr url")
    parser.add_argument("--add-ssr", metavar="ssr_url", help="add ssr node")
    parser.add_argument("--test-again", metavar="ssr_node_id", type=int, help="test ssr node again")
    parser.add_argument("--print-qrcode", metavar="ssr_node_id", type=int, help="print ssr node qrcode")
    parser.add_argument("--setting-global-proxy", action="store_true", help="setting system global proxy,only support Ubuntu Desktop")
    parser.add_argument("--setting-pac-proxy", action="store_true", help="setting system pac proxy,only support Ubuntu Desktop")
    parser.add_argument("--close-system-proxy", action="store_true", help="close system proxy,only support Ubuntu Desktop")
    parser.add_argument("--setting-auto-start", action="store_true", help="setting ssr auto start")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.list:
        d.displaySSRList()
    elif args.update:
        u.updateSubscribe()
    elif args.config:
        pass
    elif args.fast_node:
        h.startFastNode()
    elif args.start:
        h.start(id=args.start, port=args.port)
    elif args.stop:
        h.stop(id=args.stop, port=args.port)
    elif args.version:
        pass
    elif args.setting_url:
        u.updateSubcribeUrl(args.setting_url)
    elif args.setting_address:
        u.updateLocalAddress(args.setting_address)
    elif args.list_url:
        d.displaySuscribeUrl()
    elif args.add_url:
        pass
    elif args.remove_url:
        pass
    elif args.list_address:
        d.displayLocalAddress()
    elif args.parse_url:
        d.parseSSRUrl(args.parse_url)
    elif args.add_ssr:
        pass
    elif args.test_again:
        pass
    elif args.print_qrcode:
        pass
    elif args.setting_global_proxy:
        pass
    elif args.setting_pac_proxy:
        pass
    elif args.close_system_proxy:
        pass
    elif args.setting_auto_start:
        pass
    elif args.test_speed:
        u.testSSRSpeed()
    else:
        parser.print_help()

if __name__ == "__main__":
    # sss
    main()
