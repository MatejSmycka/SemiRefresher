# SemiRefresher

---

## Installation:
You need your own cookies:
1. Go to the IS website, 
2. Hit f12 button
3. In chrome go to "Aplication" then "Storage"
4. find "iscreds" and "issession" in "Cookies" and replace values in "URLs.py" with values from your cookies. 

cookies = {
    'iscreds': 'YOUR CREDS',
    'issession': 'YOUR SESSION',
 }
 
Also replace url with your desirated one, you can also add multiple urls.

urls=[
"https://is.muni.cz/auth/seminare/student?fakulta=1433;obdobi=8403;studium=1073518;predmet=1405689;prihlasit=646196;akce=podrob;provest=1;stopwindow=1;design=m",
"https://is.muni.cz/auth/seminare/student?fakulta=1433;obdobi=8403;studium=1073518;predmet=1405689;prihlasit=646196;akce=podrob;provest=1;stopwindow=1;design=m",
"https://is.muni.cz/auth/seminare/student?fakulta=1433;obdobi=8403;studium=1073518;predmet=1405689;prihlasit=646196;akce=podrob;provest=1;stopwindow=1;design=m"]

 ---
## Usage:

$pip3 freeze > requirements.txt

$python3 SemiRefresher


 ---

Tip: You can try script on seminars you have already signed up for.
