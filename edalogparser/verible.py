from .base import LogParser, LogEntry, Log
import re

class VeribleLintLogParser(LogParser):
  regex = re.compile(r"^(.*?):(\d+):(\d+): (.*) \[Style: (.*?)\]")

  def __init__(self):
    super().__init__()

  def parse(self, log):
    entries = Log()
    for line in log:
      m = self.regex.match(line)
      if m:
        severity = "warning"
        msg = m.group(4)
        file = m.group(1)
        line = m.group(2)
        col = m.group(3)
        code = m.group(5)
        entries.append(LogEntry(severity=severity, msg=msg, file=file, line=line, col=col, code=code))
    return entries
