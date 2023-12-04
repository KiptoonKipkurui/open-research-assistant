#!bin/bash
set -eu

mkdir ../models

# URL of the model to download
url="https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin"
curl -o ../models/llama-2-7b-chat.ggmlv3.q4_0.bin "$url"

