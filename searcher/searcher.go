package searcher

func NewDefaultLinuxSearcher(isStdin bool, path string) *Grep {
	return NewGrep(isStdin, path)
}

func NewDefaultWindowsSearcher(isStdin bool, path string) *SelectString {
	return NewSelectString(isStdin, path)
}
