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

# OPEN-RESEARCH ASSISTANT
## Introduction
Open-Research Assistant is a state of the art inference engine that allows you to interogate textual PDF documents of all nature from scientific to fiction and derive insights from it. It is powered by open-source Large Language Models and uses Retrieval Augmentated Generation to enhance the knowledge base of the LLM and reduce hallucinations that commonly affect LLMs. Its main features are
* Upload of Local PDF document or donwload of online PDF documents.
* Calculation and storage of Vector embeddings of PDF documents.
* Configurable Text Chunking according to an LLMS token length
* Document queries response with source documents in under 2.5 minutes.
* Support for LLMS with 3B or 7B parameters.  

## Installation Instructions
### Prerequisites
Due to the enoumous size of Large Language Models, this project does not come batteries included in terms of the LLM model. One is therefore required to independently download the LLM 

The program is python based, and so requires python < 3.11

The model can be downloaded from the following endpoint
[llama2 7B LLM](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin)
 from [huggingface](https://huggingface.co). Hugging Face is the hub of everything Machine Learning and AI including to but not limited to being an Open-Source LLM repository.

 Once downloaded, the model should be placed in the [models](./models/) directory. This model can then be used for reference

 ### Installation
 Open-Research assistant has several options for installation as listed below
- Makefile
- Manual
- Docker Compose

No matter the installation method, the open research assistant would run at `localhost:8000` so any processes running at this port should be stopped before running this project.
#### Makefile
The Makefile is a shell utility used to automate common functions. It is natively supported in linux based systems but also available to Windows based systems after jumping through some hoops. The open-research assistant comes with a Makefile with several functionalities to enable easy installation and running of the program. 
To run the project, run the following command
```sh
make run
```  
The command will:
* Create a virtual environment
* Install the required packages
* Run the program

### Manual Installation
Open-Research Assistant can also be installed manually by cloning the project and running the following steps

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
  This application utilizes a couple of packages defined in the [requirements file](./requirements.txt). They cann be installed by the following command

  ```sh
  pip install -r requirements.txt
  ```
  <li>Run the application</li>

  Finally, run the application using `uvicorn`

  ```sh
  uvicorn main:app
  ```
</ol> 

### Docker-Compose

This option utilizes the docker ecosystem and allows running of the application via a Docker Image. This method does not require creation of a virtual environment or installation of any packages. It however builds an Image before enventually running it. 
<br><em><strong>Important</strong></em><br>
Due to the compute intensive nature of the Open-Research Assistant, Docker should be allowed to access the Maximum resources in a the running computer. Typically atleast `8GB` of RAM and `8 processors`. Appropriate instructions to adjust this limits can be found here for [docker ce](https://docs.docker.com/config/containers/resource_constraints/) and [docker desktop](https://docs.docker.com/desktop/settings/windows/)

Having met the prerequisite requirements, The following command will utilize this [docker compose file](./docker-compose.yaml)to set up the `redis server` and `open-research-assistant` containers and expose the application at the same port as above

```sh
docker-compose up
```

<br><em><strong>Note</strong></em><br>
The docker image is quite large `~18GB` and so will take sometime and require relatively fast internet to download the required dependencies. It is common to run out of disk space assigned to docker due to the size of this image and hence special care should be taken to ensure enough disk space is available for building the docker image

## Contributing
The open-research-assistant is free to use and redistribute and thereby being an open-source project, contributions are welcomed. The [contribution guide](./contributing-guide.md) forms the first entry point for anyone willing to make contributions to this project. It documents the steps necessary to configure your development environment to be able to contribute to this project.

## Issues
Any issues discovered for this project should be opened on [GitHub](https://github.com/KiptoonKipkurui/open-research-assistant/issues) and shall be addressed by a maintainer.
