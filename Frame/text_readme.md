1. Functional Testing:

1.1 Register for Use Case Testing:
Test 1: The account does not exist
Enter: account name, password
Operation: Open the system login page, click Sign In, enter the registration interface, enter accounts(admin123), password(123456)
Output: Prompts the user to "The account has been created" and returns to the login screen
Test 2: The account already exists
Precondition: The account exists in the system
Enter: account name, password
Operation: Open the system login page, click Sign In, enter the registration interface, enter accounts(admin123), password(123456)
Output: Prompts the user to "The account has been created" and returns to the login screen

1.2 Login Use Case Test:
Test 1: Enter the correct account and password
Enter: account number, password.
Operation: Open the system login page and enter accounts(admin123), password(123456)
Output: Administrator logs in to the system home page
Test 2: Enter the wrong username or wrong password
Precondition: The user exists in the system but the password is incorrect|The user does not exist in the system
Enter: account number, password.
Steps: Open the system login page and enter accounts(admin) password(123456)
Output: Prompts user "Login failed! Wrong username or password"

1.3 Upload Photo Use Case Test: 
Test 1: Upload successfully
Input: Photo (.png, .jpg format)
Operation: Click Upload on the home page of the system, select the photo in the local folder to upload, record the photo and the corresponding upload time, and describe it in the local and database
Output: Prompts the user to "Upload Complete"
Test 2: Upload failed
Preset: The photo description already exists
Input: Photo (.png, .jpg format)
Operation: Click Upload on the home page of the system, select the photo in the local folder to upload, and cancel the upload if you find that the photo already exists
Output: Prompts user "Upload failed"

1.4 Delete Photos:
Test 1: The photo is present
Preset conditions: Enter the home page of the system, and the photo exists
Enter: a name for the photo
Action: Click Delete, enter the name you want to delete, find a matching photo, and the photo will be removed from the database and local storage
Output: Prompts the user "Deletion Complete"
Test 2: The photo does not exist
Preset condition: Enter the home page of the system, the photo does not exist
Enter: a name for the photo
Action: Click Delete, enter the name you want to delete, if the photo is not found, the photo will be removed from the database and local storage
Output: Prompts the user "The photo does not exist"

1.5 Display photos
Preset: Enter the system
Input: None
Action: Click Show
Output: Browse the page showing all the photo information details

1.6. Smart Photo Search
Test 1: The photo is present
Preset: Enter the system
Input: Text description (e.g. "beach", "birthday party", etc.)
Operation: Click Find, enter a text description, compare it with the stored photo, find the corresponding photo, and output the photo
Output: Corresponding photo
Test 2: The photo does not exist
Preset: Enter the system
Input: Text description (e.g. "beach", "birthday party", etc.)
Operation: Click Find, enter a text description, compare with the stored photo, no corresponding photo found, and remind
Output: Prompts the user "The photo does not exist"