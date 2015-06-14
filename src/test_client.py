#!/usr/bin/python

import traffic
import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument("--connect", type=str, help="hostname:port")
parser.add_argument("--interval", type=int, help="summary interval")
parser.add_argument("clients", type=str, nargs="+", metavar="C", help="Clients to get summary for")

if __name__ == "__main__":
    args = parser.parse_args()

    end = datetime.now()
    start = end - timedelta(hours=args.interval)
    with traffic.Connection("tcp://" + args.connect) as c:
        summary = traffic.get_summary(c, start, end, args.clients)
    for entry in summary.data:
        print entry.address, entry.sum_traffic_in, entry.sum_traffic_out
    
    
