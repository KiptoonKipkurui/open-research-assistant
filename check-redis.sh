#!/bin/bash

# Function to check if Redis server is running
check_redis() {
  # Use pgrep to check if redis-server process is running
  if pgrep redis-server > /dev/null; then
    echo "Redis server is running."
  else
    echo "Redis server is not running. Starting Redis..."
    # Start Redis server (adjust the command as needed based on your setup)
    redis-server &
    echo "Redis server started."
  fi
}

# Call the function to check Redis status
check_redis
