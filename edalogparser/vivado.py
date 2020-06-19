from .base import LogParser, LogEntry, Log
import re

class VivadoLogParser(LogParser):
  regex = re.compile(r"^((INFO|WARNING|ERROR): \[(.*?)\] (.*?)( \[(.*?)\])?)\n$")

  def __init__(self):
    super().__init__()

  def parse(self, log):
    entries = Log()
    for line in log:
      m = self.regex.match(line)
      if m:
        severity = m.group(2).lower()
        msg = m.group(4)
        file = None
        line = None
        if m.group(6):
          colon = m.group(6).rfind(":")
          file = m.group(6)[0:colon]
          line = m.group(6)[colon+1:]
        entries.append(LogEntry(severity, msg, file, line, None))
    return entries

