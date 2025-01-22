Linux Commands Guide - Web Application
====================================

I have done some research on how to make websites in the past and I believe knowing how to build websites can 
help my cybersecurity career. I have done some extra research to help my websites design.
I have used the following links to help me code some features on my website:
https://csspro.com/css-3d-buttons/
https://www.youtube.com/watch?v=7Xyg8Ja7dyY
https://www.youtube.com/watch?v=CqBEmgkR_fQ

Prerequisites:
------------
- Python 3.x
- Flask framework

Installation
------------

1. You can double click on folder and click on "New Terminal At Folder"

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv or python3 -m venv venv
   source venv/bin/activate  # Or Windows use: venv\Scripts\activate
   ```

3. Install required packages:
   ```
   pip install flask
   ```

Running the Application
1. Run the Flask application:
   ```
   python assessment.py or python3 assessment.py
   ```

2. Open your web browser and visit webserver when prompted


Features
--------
- Interactive command guide divided into three categories:
  * Navigation
  * File Management
  * File Content
- Animated typing examples for each command
- Cyberpunk-themed UI with glitch effects
- Loading screen animation

Project Structure (Make sure this is correct)
---------------
- assessment.py: Main Flask application file
- templates/
  * home.html: Main webpage template
  
Troubleshooting
-------------
- If the site doesn't load, ensure Flask is installed
- Check that you're in the correct directory when running the application
- Verify that port 5000 is not in use by another application

Note: press CTRL+C in the terminal to stop. 
