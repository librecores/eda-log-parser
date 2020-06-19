# EDA Log Parser

This parses the output of EDA tools and generates a list of messages with their
severity.

Install:

```bash
pip install edalogparser
```

Example: Pipe Verilator output through it to generate json:

```bash
verilator ... 2>&1 | eda-log-parser -t verilator -f json
```

Supported tools:

- `verilator`: Verilator
- `vivado`: Xilinx Vivado

Supported targets:

- `azure`: LogIssue commands for Azure Pipelines
- `dict`: Plain Python dict
- `ghactions`: Log commands for GitHub Actions
- `json`: JSON file (difference to dict: JSON strings)
