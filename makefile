.PHONY: live
live:
	air \
		--build.cmd="go build -o ./tmp/main main.go -tags='gui'" \
		--build.bin="./tmp/main" \
		--build.exclude_dir="tmp,vendor" \
		--build.exclude_regex="*_test.go"

