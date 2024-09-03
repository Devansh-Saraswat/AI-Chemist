# IntelliChem AI
IntelliChem AI is a cutting-edge web application designed to revolutionize the field of chemistry by offering personalized chemical solutions and experimental recommendations. Leveraging the advanced capabilities of the Gemini 1.5 Pro model, this app utilizes artificial intelligence to evaluate user input, laboratory conditions, and specific research objectives.

With IntelliChem AI, researchers can receive tailored experiment designs, optimized chemical synthesis routes, and insightful data analysis, all aimed at enhancing research efficiency and fostering innovation. Whether you're conducting complex chemical experiments or exploring new synthesis pathways, AI Chemist provides intelligent, data-driven guidance and support to take your research to the next level.


## Features

- **Image Analysis:** Upload an image of pharmaceutical tablets, and the app will analyze the image to identify the tablets.
- **Tablet Details:** The app provides a comprehensive description of each identified tablet, including its purpose, features, and typical applications.
- **Streamlit Interface:** A user-friendly interface built with Streamlit for easy interaction.


## User Interface

Here’s a snapshot of the IntelliChem AI App’s user interface:

![UI](https://github.com/user-attachments/assets/cd0916af-69bf-4771-8d30-ff5fb5c4cca5)



## Usage

1. Open the IntelliChem AI in your web browser after running the app.
2. Upload an image of the tablets you want to analyze.
3. Provide any specific input prompt if necessary.
4. Click the "Submit" button to get detailed information about the tablets in the image.


## Installation

To run the IntelliChem AI app locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Devansh-Saraswat/ai-chemist.git
   cd ai-chemist
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**

   Make sure you have the packages listed in `requirements.txt`. Install them using:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project. Add any necessary environment variables, such as API keys. (Note: The `.env` file is not included in the repository for security reasons.)

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

   This command will start the Streamlit server and open the application in your default web browser.


## Project Structure

- **`app.py`**: The main application file containing the Streamlit app logic.
- **`requirements.txt`**: A list of Python packages required to run the app.
- **`.env`**: Environment file for storing API keys (not included in the repository for security reasons).


## Contributing

If you want to contribute to this project, please fork the repository and create a pull request with your changes.


## License

This project is licensed under the GNU-GPL-3.0 License. See the LICENSE file for more details.
