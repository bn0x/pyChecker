from checker import *
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--file', default='proxys.txt')

args = parser.parse_args()

fileData = open(args.file, 'r').readlines()
for i in fileData:
	proxyInfo = i.strip('\n').split(':')
	functionData = checkProxy(proxyInfo[0].lower(), proxyInfo[1], proxyInfo[2])
	print functionData