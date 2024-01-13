<picture>
  <p style="text-align:center;" align="center">
<a href="https://layer5.io/meshery">
<picture align="center">
<source media="(prefers-color-scheme: dark)" srcset="static\open-research-assistant.png" width="50%" align="center" style="margin-bottom:20px;">
<source media="(prefers-color-scheme: light)" srcset="static\open-research-assistant.png" width="50%" align="center" style="margin-bottom:20px;">
<img alt="Shows an illustrated light mode open research assistant logo in light color mode and a dark mode open research assistant logo dark color mode." src="static\open-research-assistant.png" width="50%" align="center" style="margin-bottom:20px;"> </picture>
</a>

<br/><br/></p>
</picture>

<p align="center">
    <em>Inference engine, answers queries on documents powered by Open-Source Large Language Models</em>
</p>

[![Tests](https://github.com/KiptoonKipkurui/open-research-assistant/actions/workflows/security-analysis.yml/badge.svg)](https://github.com/KiptoonKipkurui/open-research-assistant/actions/workflows/security-analysis.yml)
[![Linting](https://github.com/KiptoonKipkurui/open-research-assistant/actions/workflows/pylint.yml/badge.svg)](https://github.com/KiptoonKipkurui/open-research-assistant/actions/workflows/pylint.yml)
[![GitHub release](https://img.shields.io/github/release/anchore/syft.svg)](https://github.com/KiptoonKipkurui/open-research-assistant/releases/latest)
[![Python version](https://img.shields.io/badge/python-3.8|3.9|3.10-blue)](https://github.com/KiptoonKipkurui/open-research-assistant/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/KiptoonKipkurui/open-research-assistant/blob/master/LICENSE)

# OPEN-RESEARCH ASSISTANT
## Introduction
Open-Research Assistant is a state of the art inference engine that allows you to interogate textual PDF documents of all nature from scientific to fiction and derive insights from it. It is powered by open-source Large Language Models and uses Retrieval Augmentated Generation to enhance the knowledge base of the LLM and reduce hallucinations that commonly affect LLMs. Its main features are
* Upload of Local PDF document or donwload of online PDF documents.
* Calculation and storage of Vector embeddings of PDF documents.
* Configurable Text Chunking according to an LLMS token length
* Document queries response with source documents in under 2.5 minutes.
* Support for Llama LLMS with 3B or 7B parameters.  

## Installation Instructions
### Prerequisites
The following section describes the prerequisites before installation the project.
Due to the enoumous size of Large Language Models, this project does not come batteries included in terms of the LLM model. One is therefore required to independently download the LLM as with the instructions below.

1. **Python** <br>
The program is python based, and so requires python <= 3.11
2. **Model** <br> 
The model can be downloaded from the following endpoint
  [Ocra-Mini 3B](https://gpt4all.io/models/gguf/orca-mini-3b-gguf2-q4_0.gguf)
  from [GPT$All](https://gpt4all.io/index.html). GPT4All is a hub of Open-Source LLM models that can run on CPU.
  Once downloaded, the model should be placed in the [models](./models/) directory. This model can then be used for reference
3. **Redis**<br>
 The application also requires a running redis instance. Redis installation instructions can be found [here](https://redis.io/docs/install/install-redis/)
  To start the redis server the following command can be applied
  ```sh
  redis-server &
  ```

 ### Installation
 The following section describes how the open-research assistant can be installed. Due to the underlying libraries used, only Unix based operating systems are supported it is also important to note that the system has been extensively tested on the Ubuntu Operating system.

The open-research assistant runs at `localhost:8000` so any processes running at this port should be stopped before running this project.

Open-Research Assistant can also be installed by cloning the project at [open-research-assistant](https://github.com/KiptoonKipkurui/open-research-assistant) and running the following steps

<ol>
  <li>Create the virtual environment</li>

  ```sh
  python3 -m venv env
  ```

  This will create a python virtual environment to isolate the dependencies required for this application from others in the system. The created virtual environment is in a folder env
  <li>Activate the virtual environment</li>

  The python environment is activated with the following command

  ```sh
  source env/bin/activate
  ```
  <li>Install required packages</li>
  This application utilizes a couple of packages defined in the <a href="./requirements.txt">requirements file</a>. They can be installed by the following command

  ```sh
  pip install -r requirements.txt
  ```
  <li>Run the application</li>

  Finally, run the application using `uvicorn`

  ```sh
  uvicorn main:app
  ```
</ol> 

## Using Open Research Assistant
Ask one question at at time waiting until you get a response before initiating the other.

## Troubleshooting

## Contributing
The open-research-assistant is free to use and redistribute and thereby being an open-source project, contributions are welcomed. The [contribution guide](./contributing-guide.md) forms the first entry point for anyone willing to make contributions to this project. It documents the steps necessary to configure your development environment to be able to contribute to this project.

## Issues
Any issues discovered for this project should be opened on [GitHub](https://github.com/KiptoonKipkurui/open-research-assistant/issues) and shall be addressed by a maintainer.
