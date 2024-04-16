#!/usr/bin/node
// const fetchApi = fetch("https://swapi-api.alx-tools.com/api/films/")
// fetchApi.then((res) => {
//     const jsonPromise = res.json();

//     jsonPromise.then((data) => {
//         const itemNeeded = data.results[2];

//         itemNeeded.characters.forEach((element, index) => {
//             const linkApi = fetch(element)
//             linkApi.then((response) => {
//                 const linkContent = response.json();
//                 linkContent.then((data) => {
//                     console.log(`${index} - ${data.name}`);
//                 });
//             });
//         });

//     });

// });
const itemID = process.argv[2] - 1;

const fetchApi = fetch('https://swapi-api.alx-tools.com/api/films/');

fetchApi.then((res) => {
  const jsonPromise = res.json();

  jsonPromise.then((data) => {
    const itemNeeded = data.results[itemID];
    const promises = [];

    itemNeeded.characters.forEach((element, index) => {
      const linkApi = fetch(element);
      promises.push(linkApi.then((response) => response.json()));
    });

    Promise.all(promises).then((characters) => {
      characters.forEach((data) => {
        console.log(`${data.name}`);
      });
    });
  });
});
