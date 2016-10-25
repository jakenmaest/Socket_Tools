#!/usr
#/bin/python
# Socket_Tools.py 0.0.1 (Linux) - Some handy python network tools by jakes
#    Indended for use in iPython can also be imported as a library class.
#
#    linux ext deps - nmap, gcc, python-dev
#    python ext deps - netifaces, python-nmap,

import os, sys, re, netifaces, nmap

class SocketTools:
  # Socket Library Class
  def __init__(self):
      pass

  # Extract IPv4 Addresses from a string or file. Outputs to list
  # TODO: Validate IP's
  #       File output (json, xml)
  #       Include file stream buffering to cut down on overhead on file extraction
  def extIPFile(inFile):
      # If file is valid, read it and place all IPs in a list
      if os.path.isfile(inFile)!=1: 
          # print "\nfile \'"+inFile+"\' is not valid"
          return "invalid file"
      else:
          file = open(inFile,'r')
          fileStr = file.read()
          ipListTmp = re.findall(r'[0-9]+(?:\.[0-9]+){3}', fileStr)
          # Remove duplicates * Also scrambles order *
          ipList = list(set(ipListTmp))
          return ipList  
  def extIPString(inStr):
      strTmp = str(inStr)
      ipListtmp = re.findall(r'[0-9]+(?:\.[0-9]+){3}', )
      # Remove duplicates * Also scrambles order *
      ipList = list(set(ipListtmp))
      return iplist
  
  # Some network interface tools based on netifaces by Alistair Houghton

  # get Network interface list
  def getNetIfaces():
      return netifaces.interfaces()
  
  # Get address information about specified interface
  def getIfAddressInfo(iface):
      return netifaces.ifaddresses(iface)

  # get internet gateway
  def getInetGateway(iface):
      addrs = netifaces.ifaddresses(iface)
      if addrs[netifaces.AF_INET] != "":
         return addrs[netifaces.AF_INET]
      else: return "Not Connected to Internet"

  # get all network gateways
  def getGateways(self):
      netifaces.gateways()

  # Some scanning tools using nmap command line by Gordon "Fyodor" Lyon, or nmap-python by Alexadra Norman
  
  # scan local network by interface; if bash is set to true the output will be returned with popen
  def nmscanIfaceLocal(iface, args, bash=false):
      ipListStr = ""
      ipList = get
      nm = nmap.PortScanner()
      nm.scan('localhost')

  
