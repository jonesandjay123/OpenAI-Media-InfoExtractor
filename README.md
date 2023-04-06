# OpenAI-Media-InfoExtractor

This project aims to extract and analyze text from video and audio content, in order to present an outline or summary of the content.

## Prerequisites

- Python 3.x

## Setting Up the Development Environment

1. Clone or download the project.
2. In the project root directory, create and activate a virtual environment (only needed for the initial setup):
   - macOS or Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
3. After activating the virtual environment, install the required dependencies with `pip install -r requirements.txt`.
4. To clean up the `requirements.txt` file and remove unused dependencies, install `pipreqs` using `pip install pipreqs`.
5. Run `pipreqs . --force` to generate a new `requirements.txt` file with only the necessary dependencies. This command will overwrite the existing `requirements.txt` file.

## Working with the Virtual Environment

- Activate the virtual environment: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows).
- Install or update packages: `pip install -r requirements.txt`.
- Update the `requirements.txt` file after adding or updating dependencies: `pip freeze > requirements.txt`.
- Exit the virtual environment: `deactivate`.

Remember to activate the virtual environment and update the `requirements.txt` file as needed while working on the project.
