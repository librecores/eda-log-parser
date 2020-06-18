from .base import LogParser, LogEntry, Log
import re

class VerilatorLogParser(LogParser):
  regex_nofl = re.compile(r"%((Warning|Error)-\w+: ([^%]*))")
  regex_fl = re.compile(r"(.*?):(\d+):(\d+): (.*)")

  def __init__(self):
    super().__init__()

  def parse(self, log):
    log = "".join(log)
    entries = Log()
    for m in self.regex_nofl.finditer(log):
      severity = m.group(2).lower()
      msg = m.group(3).replace("\n", "\\n")
      m = self.regex_fl.match(msg)
      if m:
        file = m.group(1)
        line = int(m.group(2))
        col = int(m.group(3))
        msg = m.group(4)
        entries.append(LogEntry(severity, msg, file, line, col))
      else:
        entries.append(LogEntry(severity, msg, None, None, None))
    return entries

