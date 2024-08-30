[![Readme PT-BR](/assets/readme-pt-br.svg)](/docs/readme/readme-pt-br.md)

![Logo](/assets/arctracker-logo.svg)

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

## Optional Requirements

The application no required dependencies, but it has some optional dependencies that improve performance, such
as [ripgrep](https://github.com/BurntSushi/ripgrep) for the recursive search in
the directory and in Stdin, and [jq](https://github.com/jqlang/jq) for the
formatting of ripgrep's result.

Below are the installations steps for each tool:

- [ripgrep](https://github.com/BurntSushi/ripgrep?tab=readme-ov-file#installation)
- [jq](https://github.com/jqlang/jq?tab=readme-ov-file#installation)

## Installation

To install the program, simply download the binary in the latest
[release](https://github.com/marcelo-fm/arctracker/releases) page, or you can
install it with go by executing:

```go
go install github.com/marcelo-fm/arctracker@latest
```

## Debian and Ubuntu

You can download the .deb package through the latest [release](https://github.com/marcelo-fm/arctracker/releases)
and install it with `dpkg`. Below is an example in one line for the release tag _1.1.0_:

```bash
curl -L -o https://github.com/marcelo-fm/arctracker/releases/download/v1.1.0/arctracker_1.1.0-1_amd64.deb && sudo dpkg -i arctracker_1.1.0-1_amd64.deb
```

I'm working in creating packages for most linux distros and windows package managers.

## Usage

ArcTracker has two ways of using it. First is by recursively searching for arcpy tools used within a project. To do that, simply pass the path of the directory to view a interactive table of the tools used in the project and the level of licenses required to run them.

![ArcTracker Usage](/assets/arctracker.gif)

You can also pass the flag `--json` to return the output as JSON, or the flag `--csv` to return the output as a CSV.

The `--output` flag is used to write the JSON or CSV output into a file.
