#!/bin/bash

# Function to check if Redis is installed and running
check_redis() {
    if ! command -v redis-server &> /dev/null; then
        echo "Redis is not installed. Please install Redis."
        exit 1
    fi

    if ! pgrep -x redis-server &> /dev/null; then
        echo "Redis is not running. Please start Redis."
        exit 1
    fi

    echo "Redis is installed and running."
}

# Function to check if a specific file is present in a given folder
check_model() {
    folder="$1"
    file_to_check="$2"

    if [ ! -d "$folder" ]; then
        echo "Folder '$folder' does not exist."
        exit 1
    fi

    if [ ! -f "$folder/$file_to_check" ]; then
        echo "File '$file_to_check' not found in folder '$folder'."
        exit 1
    fi

    echo "File '$file_to_check' is present in folder '$folder'."
}

check_python(){
    # Check if Python is installed
    if command -v python &> /dev/null; then
        echo "Python is installed."
    else
        echo "Python is not installed. Please install Python."
        exit 1
    fi

}

# Usage example
check_python
check_redis
check_model "./models/" "orca-mini-3b-gguf2-q4_0.gguf"

echo "All checks passed."
