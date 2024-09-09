#!/bin/bash

GOOS=windows \
	GOARCH=amd64 \
	go build -o ./bin/arctracker.exe main.go -tags prod
