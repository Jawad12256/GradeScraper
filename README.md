# GradeScraper
⚠️⚠️ **If you are new to GradeScraper, please follow the instructions below to set it up correctly.** ⚠️⚠️

GradeScraper is a tool to collate raw marks from Blackboard into a tabulated terminal output.  
  
⚠️ **Disclaimer**: GradeScraper is designed to be used for legitimate purposes only. I am not liable for any misuse of any of the contents of this repository or any of the resulting consequences!

# Setting up GradeScraper
## Dependencies
### 0️⃣ For absolute beginners to coding
Download Python: https://www.python.org/downloads/  
Download VSCode: https://code.visualstudio.com/download
(or any other suitable IDE)
### 1️⃣ Get cookies.txt LOCALLY Chrome Extension
Download this Chrome extension: https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc  
You will use this to export a cookies file to your local machine.  
If you are not using Chrome, you will need to find a way to export a cookies.txt file in a NetScape format.
### 2️⃣ pip packages
Install the _requests_ and _tabulate_ packages with pip package manager as follows:  
  > pip install requests tabulate 
  
**If you are not familiar with pip**, please see the instructions here to install pip: https://pypi.org/project/pip/

## Getting the code on your local machine
Clone the repository to get the code on your local machine. If you are not familiar with how to do this, please see: https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop  

Alternatively, you can download the zip folder by going to the green "Code" button on the main repository page.

## You are now fully set up and ready to start using GradeScraper!  

# Using GradeScraper
## Exporting cookies.txt
Log onto the Blackboard website. With the page open, find the Get cookies.txt LOCALLY extension and click the first option, **Export**  
Save the cookies.txt file to the same folder as the code. ⚠️ **If you do not do this, you will run into errors!**

Note that cookies.txt files expire after 1-2 hours, so you will likely need to re-export from the Blackboard page each time you want to run the program.

## Running the code
Open the code in your IDE (e.g. VSCode). Run the code (in VSCode, Run > Run Without Debugging, and select Python Debugger at the top if prompted).

## Results
Your table of marks should be visible in the terminal at the bottom. It is also exported to a CSV file, _marks.csv_, in the same directory as the code.  
You may also notice a _user_id.txt_ file appearing in your directory: this just helps the code skip a few steps the next time you run it. If for whatever reason it gets modified or you have issues with it, simply delete this file in your local directory. It will be refreshed the next time you run the code.

# Troubleshooting

### ❌ Error: `API Error 401 – API request is not authenticated`
Your cookies have expired.  
**Solution:** Re-export a fresh `cookies.txt` from Blackboard.

---

### ❌ Course shows “PRIVATE”
This means the course is unavailable or archived on Blackboard.  
This is normal — the script cannot access private courses.

---

### ❌ Score shows “0.0” but should be a real number  
Some Blackboard responses include irrelevant `0` scores.  
The script filters and selects the most reasonable value, usually between 0 and 100.

---

### ❌ Path or file not found  
Ensure the following files are in the **same folder**:

- `GradeScraper.py`
- `cookies.txt`
- (After first run) `user_id.txt`

---
