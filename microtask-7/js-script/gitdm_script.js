const fetch = require("node-fetch");
const fs = require("fs");

fs.readFile("./github_users_test.json", (err, jsonString) => {
  if (err) {
    console.log("File read failed:", err);
    return;
  }
  try {
    const devs = JSON.parse(jsonString);
    devs.map((dev) => {
      fetchData(dev);
    });
  } catch (err) {
    console.log("Error parsing JSON string:", err);
  }
});

async function fetchData(dev) {
  let name = dev.name;
  let email = dev.email.replace(/!/, "@");
  let source = dev.source.replace(/[\r\n]+/gm, "");
  let username = dev.login.replace(/[\r\n]+/gm, "");
  fetch("http://localhost:8000/graphql/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query: `mutation{addIdentity(email: "${email}", name: "${name}", source: "${source}" username: "${username}") {uuid}}`,
      variables: {
        now: new Date().toISOString(),
      },
    }),
  })
    .then((res) => res.json())
    .then((result) => console.log(result));
}
