from prometheus_client import Gauge, start_http_server
import time
import nmap3
import socket
import argparse
import yaml


parser = argparse.ArgumentParser(description='Exporter for network port scanner.')
parser.add_argument('--config', help='sleep time to next probe. Default: 600 sec', type=str)
args = parser.parse_args()


if not args.config:
  parser.print_help()
  exit(1)

with open(args.config) as file:
    config_file = yaml.load(file, Loader=yaml.FullLoader)
server_port = config_file["server_port"]
update_time = config_file["update_time"]
scan_list = config_file["server_list"]


def scan_host(ipaddr):
  nmap = nmap3.NmapScanTechniques()
  results = nmap.nmap_syn_scan(ipaddr)
  ports = results[ipaddr]["ports"]
  open_ports = []
  for port_info in ports:
      if port_info["state"] == "open":
         open_ports.append({"protocol":port_info["protocol"],"portid":port_info["portid"],"reason_ttl":port_info["reason_ttl"]})
  return open_ports


if __name__ == '__main__':
  print("Start server: port " + str(server_port) + ", update time: " + str(update_time) + ", scan list " + str(scan_list) )
  reason_ttl = Gauge('portscan_reason_ttl', 'Description of gauge', labelnames=["host","protocol","portid"])
  open_port_total = Gauge('open_port_total', 'Open port total', labelnames=["host","total"])
  start_http_server(server_port)
  while True:
    for host in scan_list:
        for port_info in scan_host(host):
            reason_ttl.labels(host,port_info["protocol"],port_info["portid"]).set(port_info["reason_ttl"])
        open_port_total.labels(host,len(scan_host(host)))
    print("next update after {} sec".format(str(update_time)))
    time.sleep(update_time)