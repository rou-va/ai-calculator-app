# AI-Powered Calculator with Learning Suggestions

## 📌 Project Overview

This project is an AI-powered calculator that not only performs basic mathematical operations but also provides:

- **Step-by-step explanations** of calculations using AI.
- **Personalized learning suggestions** based on user patterns.
- A **Streamlit-based UI** for easy interaction.

The AI functionalities are powered by **Groq's deepseek-r1-distill-llama-70b model** to enhance user learning and understanding.

---

## 🚀 Features

### 🔢 Basic Calculator Operations

The calculator supports:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Exponentiation (`**`)
- Modulus (`%`)
- Expressions with multiple operands and operators (e.g., `3 + 5 * 2`)

### 🧠 AI-Generated Explanations

- The AI provides a **detailed breakdown** of the steps required to solve the inputted mathematical expression.
- Helps users **understand the logic** behind calculations.

### 🎓 Personalized Learning Suggestions

- AI analyzes the input and provides **tips** to help users improve their math skills.
- Suggestions are tailored based on the user's frequent mistakes or patterns.

---

## 🛠️ Installation and Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/ai-calculator.git
cd ai-calculator
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key

- Create a `.env` file in the project root.
- Add your **Groq API key**:

```sh
GROQ_API_KEY=your_actual_api_key_here
```

### 5️⃣ Run the Streamlit App

```sh
streamlit run app.py
```

---

## 🖥️ Usage

1. **Enter a mathematical expression** in the input field.
2. Click **Calculate**.
3. View:
   - The **calculation result**.
   - A **step-by-step explanation**.
   - A **personalized learning suggestion**.

---

## 📚 Technologies Used

- **Python** (Backend logic)
- **Streamlit** (Frontend UI)
- **Groq AI Model** (AI-generated explanations and learning suggestions)
- **dotenv** (Environment variable management)

---

## 🤝 Contributing

Feel free to open issues or submit pull requests to enhance the project.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Your message"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## 🔗 License

This project is licensed under the **MIT License**.

---

## 📩 Contact

For any inquiries or collaboration opportunities, feel free to reach out!

📧 **Email:** [your.email@example.com](mailto\:your.email@example.com)

🌍 **GitHub:** [yourusername](https://github.com/yourusername)

