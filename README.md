# PassGuard: Password Strength Analyzer


*A simple yet powerful tool to check and improve your password strength.*

---

## Overview
**PassGuard** is a Python-based web application built with Streamlit that helps users evaluate the strength of their passwords. It provides real-time feedback, a visual strength meter, and actionable tips to create secure, unbreakable passwords. Whether you're securing your social media or your bank account, PassGuard has got your back!

---

## Features
- **Password Strength Scoring:** Rates your password on a scale of 0-4 (Weak to Strong).
- **Real-time Feedback:** Get instant suggestions to improve your password.
- **Visual Strength Meter:** See your password strength with a progress bar.
- **Simple UI:** Clean, user-friendly interface powered by Streamlit.
- **Customizable Rules:** Checks for length, case diversity, digits, and special characters.

---

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RaoAsadMehmood/Password-Strength-Analyzer.git
   cd Password-Strength-Analyzer


 2.   ### Install Dependencies:
     pip install -r requirements.txt

3. ### Run the App:
       streamlit run main.py
4. ### Open your browser and go to http://localhost:8501.

 ###  Usage
Launch the app using the steps above.
Enter your password in the input field (don’t worry, it’s hidden!).
Check the strength meter and read the improvement tips.
Tweak your password until PassGuard gives you the green light!
Example
Input: pass123
Output: Weak (Missing uppercase, special characters)
Input: P@ssw0rd
Output: Strong (Meets all criteria)


### How It Works
 PassGuard evaluates passwords based on these criteria:

Length: At least 8 characters.
Case Diversity: Mix of uppercase and lowercase letters.
Digits: At least one number (0-9).
Special Characters: At least one symbol (e.g., !@#$%&*?).
A score of 4/4 means your password is Strong. Anything less comes with tips to improve.

### Future Enhancements
Integrate a common password checker to avoid weak choices.
Add multi-language support for global users.


### Contributing
Feel free to fork this repo, submit pull requests, or open issues for bugs and feature requests. Let’s make PassGuard even better together!


## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

Author
Rao Asad Mehmood
GitHub: RaoAsadMehmood
Created: March 2025