#!/bin/bash

GOOS=linux \
	GOARCH=amd64 \
	go build -o ./bin/arctracker main.go
