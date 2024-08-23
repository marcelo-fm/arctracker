-- +goose Up
-- +goose StatementBegin
CREATE TABLE licenses (
    id serial PRIMARY KEY NOT NULL,
    tool varchar(255) UNIQUE NOT NULL,
    tool_alias varchar(255) NOT NULL,
    toolset varchar(255),
    basic int NOT NULL DEFAULT 0,
    standard int NOT NULL DEFAULT 0,
    advanced int NOT NULL DEFAULT 0,
    extensions varchar(255) NOT NULL DEFAULT ''
);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
DROP TABLE licenses;
-- +goose StatementEnd
