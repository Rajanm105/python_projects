package main

import (
	"database/sql"
	"log"
	_"github.com/lib/pq"
)

var DB *sql.DB

func ConnectDB() {
	connStr := "postgres://postgres:admin@localhost:5432/go_test?sslmode=disable"
	var err error
	DB, err = sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal("Failed to connect DB: ", err)
	}
}