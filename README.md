# Random Wikipedia Article 📚

This Python script allows you to retrieve a random Wikipedia article from a specified category, such as "software development." It uses the Wikipedia-API library and integrates environment variables for sensitive data like the `user_agent`. This project is lightweight and easy to run locally.

## Features
- Fetches random articles from a specified Wikipedia category.
- Uses environment variables to store sensitive information such as the user agent.
- Easily customizable to fetch articles from any category or language supported by Wikipedia.

## How to Use It

### Prerequisites
- Python.
- Install the dependencies using `pip`.
- Create an `.env` file for environment variables.

### Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/villoslado/randomWikiArticle.git
    cd randomWikiArticle
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create an `.env` file in the root directory and add the following:
    ```env
    USER_AGENT=YourProjectName (name@example.com)
    ```

### Running the Script

Run the Python script with the following command:

```bash
python random_wiki.py
