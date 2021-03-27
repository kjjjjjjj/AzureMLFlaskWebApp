Step 0: Start VS Code -> File -> Open Folder

step 1: Terminal -> New Terminal

Step 2:
# Create the environment
python -m venv venv
# Activate the environment
.\\venv\\scripts\\activate

Step 3:
Create file requirements.txt, and add the following text:
flask
python-dotenv
requests

Step 4: Install requirements
pip install -r requirements.txt

Step 5: set FLASK_ENV=development

Step 6: pip install pyforest

Step 7: flask run