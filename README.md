# arctracker

![GitHub go.mod Go version](https://img.shields.io/github/go-mod/go-version/marcelo-fm/arctracker?style=for-the-badge) ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/marcelo-fm/arctracker/.github%2Fworkflows%2Fgo.yml?style=for-the-badge) ![GitHub Release](https://img.shields.io/github/v/release/marcelo-fm/arctracker?style=for-the-badge) ![GitHub Tag](https://img.shields.io/github/v/tag/marcelo-fm/arctracker?style=for-the-badge)

ArcGIS Licensing Tracker

ArcTracker provides an easy and interactive way to keep track of the licensing
in your arcpy python code.

## Description

ArcTracker is a CLI application that search through the ArcGIS documentation for
a tool licensing. It can be used by passing the path of a repository as an
argument, and it will scrape the licensing for each tool used in the python
scripts. It can be also used within a pipeline, by reading the command of a tool
passed in the pipeline, when executed without arguments.

## Requirements

- [ripgrep](https://github.com/BurntSushi/ripgrep)
- [jq](https://github.com/jqlang/jq)

## Installation

To install the program, simply download the binary in the latest
[release](https://github.com/marcelo-fm/arctracker/releases) page, or you can
install it with go by executing:

```go
go install github.com/marcelo-fm/arctracker@latest
```
