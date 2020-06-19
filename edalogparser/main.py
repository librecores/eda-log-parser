import sys
import argparse

from .verilator import VerilatorLogParser
from .vivado import VivadoLogParser

tools = { "verilator": VerilatorLogParser, "vivado": VivadoLogParser }

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--tool", required=True, choices=tools.keys())
  parser.add_argument("-f", "--format", choices=["json", "azure", "ghaction"], default="json")
  parser.add_argument("input", nargs='?', help="", type=argparse.FileType('r'),
                    default=sys.stdin)
  args = parser.parse_args()

  print(tools[args.tool]().parse(args.input.readlines()).get_as(args.format))
