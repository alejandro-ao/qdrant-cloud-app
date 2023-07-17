# App Boilerplate with GUI for Qdrant Managed Cloud Service

> This repository accompanies the [App Boilerplate with GUI for Qdrant Managed Cloud Service](https://youtu.be/1X6QX6Z6Zq8) video tutorial on YouTube.

This repository contains an app boilerplate with a graphical user interface (GUI) that connects to a remote database hosted in Qdrant's Managed Cloud Service. The purpose of this boilerplate is to provide a starting point for building applications that interact with a Qdrant vector database.

## Features

- Graphical user interface (GUI) for easy interaction with the Qdrant vector database.
- Seamless integration with Qdrant's Managed Cloud Service.
- Simple setup process by cloning the repository and adding your credentials to the `.env` file.
- Comes with a comprehensive set of requirements specified in the `requirements.txt` file.

## Prerequisites

Before using this app boilerplate, make sure you have the following:

- Python 3.x installed on your system.
- An active Qdrant Managed Cloud Service account.
- Your Qdrant Managed Cloud Service credentials.

## Installation

To install and run the app boilerplate, follow these steps:

1. Clone this repository to your local machine:

```shell
git clone https://github.com/alejandro-ao/qdrant-cloud-app.git
```

2. Change into the project directory:

```shell
cd qdrant-cloud-app
```

3. Install the required Python packages using pip:

```shell
pip install -r requirements.txt
```

## Configuration

To configure the app boilerplate to work with your Qdrant Managed Cloud Service account, you need to add your credentials to the `.env` file. Follow these steps:

1. Copy the `.env.example` file and rename it to `.env`:

```shell
cp .env.example .env
```

2. Open the `.env` file in a text editor and provide your Qdrant Managed Cloud Service and OpenAI   credentials:

```plaintext
OPENAI_API_KEY=

QDRANT_HOST=
QDRANT_API_KEY=
QDRANT_COLLECTION_NAME=
```

## Usage

Once you have completed the installation and configuration steps, you can run the app boilerplate using the following command:

```shell
streamlit run app.py
```

This command will start the application.

## Contributing

This repository does not accept contributions unless they are aimed at fixing errors in the original code. The code is intentionally maintained as-is to support the accompanying YouTube video tutorial.

If you discover any errors or issues in the original code, please feel free to open an issue on the GitHub repository, and we will address it accordingly.

## License

The code in this repository is available under the [MIT License](LICENSE). Feel free to modify and use it for your own projects.