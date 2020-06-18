from abc import ABC, abstractmethod
import json

class LogEntry:
  def __init__(self, severity, msg, file, line, col):
    self.severity = severity
    self.msg = msg
    self.file = file
    self.line = line
    self.col = col
  def as_dict(self, full=False):
    d = { "severity": self.severity, "msg": self.msg }
    if self.file is not None or full:
      d["file"] = self.file
      if self.line is not None or full:
        d["line"] = self.line
      if self.col is not None or full:
        d["col"] = self.col
    return d
  def as_azure(self):
    m  = "##vso[task.logissue type={}".format(self.severity)
    if self.file is not None:
      m += ";sourcepath="+self.file
      if self.line is not None:
        m += ";linenumber={}".format(self.line)
      if self.col is not None:
        m += ";columnnumber=".format(self.col)
    m += "]" + self.msg
    return m
  def as_ghaction(self):
    m = "::{} ".format(self.severity)
    if self.file is not None:
      m += "file=" + self.file
      if self.line is not None:
        m += ",line={}".format(self.line)
      if self.col is not None:
        m += ",col={}".format(self.col)
    m += "::" + self.msg.replace('%', '%25').replace('\\n', '%0A').replace('\\r', '%0D').replace("\\'", "\'")
    return m

class Log(list):
  def __init__(self):
    super().__init__()
  def get_as(self, type):
    return getattr(self,"as_"+type)()

  def as_dict(self):
    return [l.as_dict() for l in self]

  def as_json(self):
    return json.dumps(self.as_dict(), indent=4)

  def as_azure(self):
    return "\n".join([l.as_azure() for l in self])

  def as_ghaction(self):
    return "\n".join([l.as_ghaction() for l in self])

class LogParser(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def parse(self, log):
    pass

