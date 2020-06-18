# EDA Log Parser

This parses the output of EDA tools and generates a list of messages with their
severity.

Install:

```bash
pip install edalogparser
```

Pipe Verilator output through it to generate json:

```bash
verilator ... 2>&1 | eda-log-parser -t verilator -f json
```

Other targets:

- `azure`: LogIssue commands for Azure Pipelines
- `ghactions`: Log commands for GitHub Actions
