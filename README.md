# Telegram AutoResponder

An automatic auto-responder bot for Telegram that emulates your speaking style and responds as if from your account.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/YourGitHubUsername/Telegram-AutoResponder.git
    cd Telegram-AutoResponder
    ```

2. **Create a Virtual Environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:

    - For Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - For Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Generate the Session String**:
    - Replace `YOUR_API_ID` and `YOUR_API_HASH` in `generate_session.py` with your values from [my.telegram.org](https://my.telegram.org).
    - Run the script to generate the session string:

        ```bash
        python generate_session.py
        ```

    - Copy the generated session string and replace `YOUR_SESSION_STRING` in `main.py`.

6. **Replace Sensitive Data**:
    - Replace `YOUR_TELEGRAM_BOT_TOKEN` in `main.py` with your actual bot token.
    - Replace `YOUR_USER_ID` in `main.py` with your actual user ID.

## Setting Up the Service on Windows Using NSSM

1. **Download NSSM**:
    - Go to the [official NSSM website](https://nssm.cc/download) and download the latest version for Windows.

2. **Extract NSSM**:
    - Extract the downloaded archive to a convenient location, e.g., `C:\nssm`.

3. **Open Command Prompt or PowerShell as Administrator**:
    - Press `Win + X` and select **Command Prompt (Admin)** or **Windows PowerShell (Admin)**.

4. **Create the Service**:

    ```bash
    cd C:\nssm\nssm-2.29\win64
    nssm install TelegramAutoResponder
    ```

5. **Configure Service Parameters**:
    - In the opened NSSM window, configure the parameters:
        - **Path**: `C:\Users\Ryzen\Desktop\Питончики\Telegram-AutoResponder\venv\Scripts\pythonw.exe`
        - **Startup directory**: `C:\Users\Ryzen\Desktop\Питончики\Telegram-AutoResponder`
        - **Arguments**: `main.py`

    ![NSSM Setup](https://i.imgur.com/8zL2QZp.png)

6. **Start the Service**:

    ```bash
    .\nssm start TelegramAutoResponder
    ```

7. **Check Service Status**:

    ```bash
    .\nssm status TelegramAutoResponder
    ```

## Setting Up the Service on Windows via Command Line

1. **Remove Existing Service (if it exists)**:

    ```bash
    .\nssm remove TelegramAutoResponder confirm
    ```

2. **Create a New Service**:

    ```bash
    .\nssm install TelegramAutoResponder C:\Users\Ryzen\Desktop\Питончики\Telegram-AutoResponder\venv\Scripts\pythonw.exe C:\Users\Ryzen\Desktop\Питончики\Telegram-AutoResponder\main.py
    ```

3. **Configure Service Parameters**:

    ```bash
    .\nssm set TelegramAutoResponder AppDirectory C:\Users\Ryzen\Desktop\Питончики\Telegram-AutoResponder
    .\nssm set TelegramAutoResponder AppExit Default Restart
    .\nssm set TelegramAutoResponder DisplayName "Telegram AutoResponder"
    .\nssm set TelegramAutoResponder ObjectName LocalSystem
    .\nssm set TelegramAutoResponder Start SERVICE_AUTO_START
    .\nssm set TelegramAutoResponder Type SERVICE_WIN32_OWN_PROCESS
    ```

4. **Start the Service**:

    ```bash
    .\nssm start TelegramAutoResponder
    ```

5. **Check Service Status**:

    ```bash
    .\nssm status TelegramAutoResponder
    ```

## Running the Script Manually

To run the script manually, follow these steps:

1. **Activate the Virtual Environment**:

    - For Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - For Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

2. **Run the Script**:

    ```bash
    python main.py
    ```

## Telegram Terms of Service

**Note:** Using Telegram API for users may be prohibited according to [Telegram's Terms of Service](https://core.telegram.org/api/terms-of-service). Automatically sending messages from your account may lead to account suspension.
- **Recommendation:** Consider alternative approaches that do not violate the terms of service.

## Security of Data

- Store the session string and other sensitive data securely.
- Do not share the session string with third parties.

## Performance Optimization

- Installing `TgCrypto` will significantly speed up Pyrogram.
- Limit the length of the conversation context to reduce load on the model.

### Install TgCrypto

```bash
pip install tgcrypto
