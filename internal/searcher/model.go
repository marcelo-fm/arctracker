package searcher

type Matcher interface {
	GetType() string
}

type Match struct {
	Type string `json:"type"`
	Data *struct {
		Path struct {
			Text string `json:"text"`
		} `json:"path"`
		Lines struct {
			Text string `json:"text"`
		} `json:"lines"`
	} `json:"data"`
}

func (m *Match) GetType() string {
	return m.Type
}

type Summary struct {
	Data struct {
		ElapsedTotal struct {
			Human string `json:"human"`
			Nanos int    `json:"nanos"`
			Secs  int    `json:"secs"`
		} `json:"elapsed_total"`
		Stats struct {
			BytesPrinted  int `json:"bytes_printed"`
			BytesSearched int `json:"bytes_searched"`
			Elapsed       struct {
				Human string `json:"human"`
				Nanos int    `json:"nanos"`
				Secs  int    `json:"secs"`
			} `json:"elapsed"`
			MatchedLines      int `json:"matched_lines"`
			Matches           int `json:"matches"`
			Searches          int `json:"searches"`
			SearchesWithMatch int `json:"searches_with_match"`
		} `json:"stats"`
	} `json:"data"`
	Type string `json:"type"`
}

func (d *Summary) GetType() string {
	return d.Type
}

type End struct {
	Type string `json:"type"`
	Data struct {
		Path struct {
			Text string `json:"text"`
		} `json:"path"`
		BinaryOffset any `json:"binary_offset"`
		Stats        struct {
			Elapsed struct {
				Secs  int    `json:"secs"`
				Nanos int    `json:"nanos"`
				Human string `json:"human"`
			} `json:"elapsed"`
			Searches          int `json:"searches"`
			SearchesWithMatch int `json:"searches_with_match"`
			BytesSearched     int `json:"bytes_searched"`
			BytesPrinted      int `json:"bytes_printed"`
			MatchedLines      int `json:"matched_lines"`
			Matches           int `json:"matches"`
		} `json:"stats"`
	} `json:"data"`
}

func (e *End) GetType() string {
	return e.Type
}

type Begin struct {
	Type string `json:"type"`
	Data struct {
		Path struct {
			Text string `json:"text"`
		} `json:"path"`
	} `json:"data"`
}

func (b *Begin) GetType() string {
	return b.Type
}
