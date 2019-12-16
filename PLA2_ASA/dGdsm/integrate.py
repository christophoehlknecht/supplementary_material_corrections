#!/usr/bin/python3 -tt
import sys
import re
import math

###########################################################
# this script integrates over the rdf output file 'rdf.out'
# the returned number still needs to be multiplicated by
# the water number density in the box (water per cubic-nm)
###########################################################

##################################################
# simple function for reading in files by filename
def readfile(filename):
  f = open(filename, 'rU')
  file = f.read()
  return file

########################################################
# integrates over the radial distribution function
# the output of this function times the total number of
# water molecules in the box is the number of water
# molecules within the cutoff sphere
def integrate(g):

  N = 0
  dr = float(g[0][0]) #the change of the radius dr (r+-dr) is just written in the first output

  for i in range(0, len(g)):
    r = float(g[i][0])
    g_r = float(g[i][1])
    n = g_r * ((r+dr)**3 - (r-dr)**3)
    N = N + n
  return N * 4./3 * math.pi


def main():
  rdf_file = readfile("./rdf.out")
  g = re.findall('(\d+\.\d+)\s+(\d+.*\d*)', rdf_file)
  N = integrate(g)
  print("Multiply the following number with the water number density (n / nm^3)")
  print("to obtain the total number of water molecules within the cutoff sphere (n)")
  print(round(N, 4))


if __name__ == '__main__':
  main()
  
