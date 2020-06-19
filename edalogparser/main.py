import sys
import argparse

from .verible import VeribleLintLogParser
from .verilator import VerilatorLogParser
from .vivado import VivadoLogParser

tools = { "veriblelint": VeribleLintLogParser,
          "verilator": VerilatorLogParser,
          "vivado": VivadoLogParser }

class parse_dict_args(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        d = {}
        for val in values:
            k, v = val.split('=')
            d[k] = v
        setattr(namespace, self.dest, d)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--tool", required=True, choices=tools.keys())
  parser.add_argument("-f", "--format", choices=["json", "azure", "ghaction"], default="json")
  parser.add_argument("-c", "--config", nargs='*', action=parse_dict_args)
  parser.add_argument("input", nargs='?', help="", type=argparse.FileType('r'),
                    default=sys.stdin)
  args = parser.parse_args()

  print(tools[args.tool](args.config).parse(args.input.readlines()).get_as(args.format))
