from .base import LogParser, LogEntry, Log
import re

class VivadoLogParser(LogParser):
  regex = re.compile(r"^((INFO|WARNING|ERROR): \[(.*?)\] (.*?)( \[(.*?)\])?)\n$")

  def __init__(self, config):
    super().__init__(config)

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
          file = self.filter_filename(m.group(6)[0:colon])
          line = m.group(6)[colon+1:]
        code = m.group(3)
        entries.append(LogEntry(severity=severity, msg=msg, file=file, line=line, code=code))
    return entries

