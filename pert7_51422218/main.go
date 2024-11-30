//No 2
package main

import (
	"fmt"
	"log"
	"net/http"
	"pert7_51422218/configs"
	"pert7_51422218/handlers"
	"pert7_51422218/middlewares"

	_ "github.com/go-sql-driver/mysql"
)

//No 2
func main() {
    PORT := 8081 

    configs.ConnectDB()
    if configs.DB == nil {
        log.Fatal("Database connection failed")
    }
    defer func() {
        if err := configs.DB.Close(); err != nil {
            log.Printf("Error closing database connection: %v", err)
        }
    }()

    mux := http.NewServeMux()
    fileServer := http.FileServer(http.Dir("catalog"))
    mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        handlers.ServeStaticFile(w, r, "catalog", fileServer)
    })
    mux.HandleFunc("/api/games/", handlers.HandleGames)
    mux.HandleFunc("/api/games", handlers.HandleGames)

    // Apply middleware
    loggedMux := middlewares.LogRequestHandler(mux)

    fmt.Printf("Server berjalan di http://localhost:%d\n", PORT)
    log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", PORT), loggedMux))
}