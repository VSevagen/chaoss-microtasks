import re
import requests
import simplejson as json

USERNAME_REGEX = "^(.+?):"
EMAIL_REGEX = ":\s(.*)"
ORGANISATION_FIRST_REGEX = "^\s(.*)*"
DATE_REGEX = "\b\d{4}-\d\d?-\d\d?\b"

USERNAME = None
EMAIL = None
ORG = None
DATE_FROM = None
DATE_UNTIL = None
PREVIOUS_USERNAME = None

with open("test_developers_affiliations.txt", "r") as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '':  # The EOF char is an empty string


        try:
            username = re.match(USERNAME_REGEX, line).group(0)
            username = username.translate({ord(':'): None})
            email = re.search(EMAIL_REGEX, line).group(0)
            email = email.translate({ord(':'): None})
            email = email.replace(" ","")
            email = email.replace("!","@")
            email = email.split(sep=",", maxsplit=2)

            NEW_USERNAME = username

            if not USERNAME:
                USERNAME = username

            if USERNAME != NEW_USERNAME:
                USERNAME = NEW_USERNAME
                EMAIL = None
                ORG = None
                DATE_FROM = None
                DATE_UNTIL = None

            if not EMAIL:
                EMAIL = email

        except:
            org = re.match(ORGANISATION_FIRST_REGEX, line).group(0)
            org = org.lstrip()
            if "from" in org:
                NEW_ORG = org_name
                org_name = org.split("from")[0]

                if not ORG:
                    ORG = org_name
                else:
                    if(ORG != NEW_ORG):
                        ORG = NEW_ORG

                date = re.findall(r'\b\d{4}-\d\d?-\d\d?\b', line)
                date_from = date[0]
                DATE_FROM = date_from
                if len(date) == 2:
                    date_until = date[1]

                    if not DATE_UNTIL:
                        DATE_UNTIL = date_until

                else:
                    date_until = "Now"
                    if not DATE_UNTIL:
                        DATE_UNTIL = date_until

            else:
                org_name = org.split("until")[0]
                NEW_ORG = org_name

                if not ORG:
                    ORG = org_name
                else:     
                    if(ORG != NEW_ORG):
                        ORG = NEW_ORG

                date = re.findall(r'\b\d{4}-\d\d?-\d\d?\b', line)
                if len(date) > 0:
                    date_until = date[0]
                    date_from = "Not found"

                    if not DATE_FROM:
                        DATE_FROM = date_from

                    if not DATE_UNTIL:
                        DATE_UNTIL = date_until
                
        if USERNAME is not None and EMAIL is not None and ORG is not None:
            url = 'http://localhost:8000/graphql/'
            query = { 'mutation($paramUsername: String $paramEmail: String){addIdentity(email: $paramEmail source:"Affiliation Files" username: $paramUsername){uuid}}' }
            params = {'paramUsername': USERNAME, 'paramEmail': EMAIL[0]}
            new_params = json.dumps(params)
            resp = requests.post(url = url, params={'query':query, "variables": new_params})
            print(resp)

        line = reader.readline()
