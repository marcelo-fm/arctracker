.PHONY: live
live:
	go tool air \
		--build.cmd="go build -o ./tmp/main -tags=gui main.go" \
		--build.entrypoint="./tmp/main" \
		--build.exclude_dir="tmp,vendor"

