import os, re, time
import requests

u_name = "natas4"
pasword = "QryZXc2e0zahULdHrtHxzyYkj59kUxLQ"
f_name = "natas0.txt"

# Username: natas0
# Password: natas0
# URL:      http://natas0.natas.labs.overthewire.org


with open(f_name, "a") as f:
    r = requests.get(
        f"http://{u_name}.natas.labs.overthewire.org/",
        
        auth=(u_name, pasword),
    )
    text_data = r.text
    print(text_data)
    # nm, pwd = text_data.split(':')
    # # save_data = re.findall("natas4(.*)", text_data)
    # save_data_to_file = f.write(f"username-> {nm} password-> {pwd}")

    # Using regex to extract the username and password
    # match = re.match(r"([^:]+):([^:]+)", text_data)
    # if match:
    #     save_data_to_file = f.write(
    #         f"username-> {match.group(1)} password-> {match.group(2)}"
    #     )
