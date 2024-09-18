.PHONY: live
live:
	air \
		--build.cmd="go build -o ./tmp/main main.go" \
		--build.bin="./tmp/main gui --loglevel=0" \
		--build.exclude_dir="tmp,vendor" \
		--build.exclude_regex="*_test.go"

