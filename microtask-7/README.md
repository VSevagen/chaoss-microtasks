## Microtask-7

Create a script that can parse gitdm developer affiliation files and load the data in a SortingHat database using GraphQL<br><br>

As you can see, there are two folders, python and js-script. In <code>js-script</code>, I used the <code>github_users.json</code> file instead of the <code>developers_affiliations.txt</code> as it was easier to fetch the required fields that with a simple text file.<br>
With the <code>python</code> folder, I used the affiliations text file.

### js-script

The developer affiliation files available in the gitdm repository are in a .txt format which makes it difficult to retrieve specific information. However all the content in the affiliation text files are provided in JSON format [here](https://github.com/cncf/devstats/blob/master/github_users.json)<br>
Using the JSON file, I was able to make a script that filters out the required attributes(name, email, source etc...) and parse them onto a GraphQL query. The Fetch API is used to make the request.<br><br>

### Steps

1. Run <code>npm install</code> to install the dependencies
2. Run <code>node gitdm_script.js</code> to run the file.

The query used is <code>ADD_IDENTITY</code>. However, that can be swapped out with another other mutations available in <code>apollo/mutations.js</code>

Here is a small demo. The origin github_users file was way too large. I'm using the <code>github_users_test.json</code> for the demo.

![ScriptDemo](js-script/js_script.gif)

### python

The developer affiliations files are in <code>.txt</code> format. So first we need to extract the information required from it. I've classified the data to be extracted as

- <code>USERNAME</code>
- <code>EMAIL</code>
- <code>ORG</code>
- <code>DATE_FROM</code>
- <code>DATE_UNTIL</code>

### Steps

1. Run <code>python gitdm_script.py</code>

Here is a small demo. The origin developers_affiliations.txt file was way too large. I'm using the <code>test_developers_affiliations.txt</code> for the demo.

![ScriptDemo](python/py_script.gif)
