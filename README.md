
# **Enterprise Communication Leak Detector (ECLD)**

## **Description**
The ECLD (Enterprise Communication Leak Detector) is a system designed to analyze messages and detect sensitive content. It helps prevent the leakage of critical information in internal and external communications. This project is ideal for companies aiming to protect their confidential data.

---

## **Features**
- **Real-Time Analysis**: Detects sensitive keywords in messages.
- **Interactive Dashboard**: Minimalist interface to input and analyze messages.
- **Security Alerts**: Notifies if sensitive content is detected.
- **Message Logs**: Stores logs of analyzed messages for auditing.

---

## **Technologies Used**
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Text Analysis**: Simple algorithm for detecting sensitive keywords
- **Animations**: CSS and Lottie Player
- **Database (simulated)**: In-memory list for message storage

---

## **Requirements**
Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **pip** package manager
- A web browser (Chrome, Firefox, etc.)

---

## **Steps to Run the Project**

### **1. Clone the Repository**
Use the following command to clone the repository:
```bash
git clone https://github.com/cleitin7/ecld-project.git
```

### **2. Navigate to the Directory**
Go to the project folder:
```bash
cd ecld-project
```

### **3. Install Dependencies**
Install the required libraries for the Flask backend:
```bash
pip install flask
```

### **4. Start the Server**
Run the Flask server:
```bash
python leak_detector.py
```
You should see this message in the terminal:
```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### **5. Access the Project**
Open your web browser and go to:
```
http://127.0.0.1:5000/
```

---

## **How to Use**

### **1. Login Page**
- Enter the **email** and **password** to log in.
- Use the following credentials:
  - **Email:** `admin@example.com`
  - **Password:** `password123`
- Click **Sign In** to proceed to the dashboard.

### **2. Dashboard Page**
- Fill in the following fields:
  - **Enter Field 1 (Subject):** Input the subject of the message.
    - Example: `"Confidential Report"`
  - **Enter Field 2 (Message Content):** Input the message content to be analyzed.
    - Example: `"Bank account: 123456789"`
  - **Enter Email (Recipient Email):** Input the recipient's email.
    - Example: `"recipient@example.com"`
- Click the **Analyze** button.

### **3. Result**
- If sensitive keywords are detected, an **alert** will appear.
- If there are no issues, a success message will be displayed.

---

## **Test Examples**

### **Sensitive Message**
- **Field 1:** `"Finance Update"`
- **Field 2:** `"Please send this to the bank. Account: 987654321"`
- **Email:** `"finance@example.com"`

**Expected Result:** Sensitive content alert.

### **Normal Message**
- **Field 1:** `"Meeting Notes"`
- **Field 2:** `"Let's schedule a meeting for tomorrow."`
- **Email:** `"team@example.com"`

**Expected Result:** Message analyzed successfully.

---

## **File Structure**
The project is organized as follows:
```
ecld-project/
│
├── templates/
│   ├── login.html          # Login page
│   ├── index.html          # Dashboard page
│
├── leak_detector.py         # Flask backend
├── README.md                # Project documentation
```

---

## **Future Improvements**
- Integration with corporate email APIs (Gmail, Outlook).
- Add user authentication with a database.
- Advanced analysis using NLP models.

---

## **Contact**
For more details or issues, feel free to reach out:
- **Discord:** nitielc7
