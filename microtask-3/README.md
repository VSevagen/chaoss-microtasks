## Microtask-3

Based on the elasticsearch documents produced by micro-mordred and source code of chaoss/grimoirelab-elk, answer the questions.

1. What is the meaning of the JSON attribute <code>author_id</code> ? <br><br>
   <code>author_id</code> is one of the identifiers provided by SortingHat. Each profile fetched from SortingHat can have 1 or more identities. Each identity will have an id which will be unique.

   ```
   "author_id":"7e51a959bcd70ff8a179d8db3ff9b3c9964b8269","author_uuid":"7e51a959bcd70ff8a179d8db3ff9b3c9964b8269","author_user_name":"valeriocos","author_domain":"bitergia.com"
   ```

   <br><br>

2. What is the meaning of the JSON attribute <code>author_org_name</code> ?<br><br>
   <code>author_org_name</code> refers to the organisation that the individual is currently enrolled in.
   Example: <code>'author_org_name': "Bitergia",</code>

<br><br>

3. What is the meaning of the JSON attribute <code>author_uuid</code> ?<br><br>
   Every author will have a unique id, <code>author_uuid</code> It might seem similar to <code>author_id</code> but in the case where we have to count number of authors, <code>author_uuid</code> is used.

```
FIELD_COUNT = 'author_uuid'  # field used to count Authors
```

- The reason being that uuid refers to the actual profile of an author, while id refers to an identity. A profile can have several identities but each profile is unique.

<br><br>

4. What is the meaning of the JSON attribute <code>author_domain</code> ?<br><br>
   <code>author_domain</code> refers to the domain of a particular profile/individual.
   Example: <code>"author_name":"Santiago Dueñas","author_domain":"bitergia.com"</code>
   <br><br>

5. What is the meaning of the JSON attribute <code>uuid</code> ?<br><br>
   <code>uuid</code> is the one attribute that uniquely identifies every item that is fetched.
   Usually it is used to identify or find any specific data (profile, item, etc...)

```
def get_profile_sh(self, uuid):
        profile = {}

        u = self.get_unique_identity(uuid)
        if u.profile:
            profile['name'] = u.profile.name
            profile['email'] = u.profile.email
            profile['gender'] = u.profile.gender
            profile['gender_acc'] = u.profile.gender_acc

        return profile
```

<br><br>

6. What is the meaning of the JSON attribute <code>utc_commit</code> ?<br><br>
   <code>utc_commit</code> refers to the commit data in UTC.
   Example: <code>"utc_commit":"2018-07-23T09:19:30"</code>
   <br><br>

7. What is the meaning of the JSON attribute <code>origin</code> ?<br><br>
   <code>origin</code> is the URL of the Github repository, where the repository being the source of the data to be fetched.
   Example: <code>"origin": "https://patternfly.atlassian.net"</code>
