#!/usr/bin/node
const request = require('request');
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

// const itemID = process.argv[2] - 1;

// const fetchApi = fetch('https://swapi-api.alx-tools.com/api/films/');

// fetchApi.then((res) => {
//   const jsonPromise = res.json();

//   jsonPromise.then((data) => {
//     const itemNeeded = data.results[itemID];
//     const promises = [];

//     itemNeeded.characters.forEach((element, index) => {
//       const linkApi = fetch(element);
//       promises.push(linkApi.then((response) => response.json()));
//     });

//     Promise.all(promises).then((characters) => {
//       characters.forEach((data) => {
//         console.log(`${data.name}`);
//       });
//     });
//   });
// });

request('https://swapi-api.alx-tools.com/api/films/', (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const itemNeeded = data.results[2];
    const characters = itemNeeded.characters;
    const promises = [];

    characters.forEach((element, index) => {
      promises.push(new Promise((resolve, reject) => {
        request(element, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            resolve({ index, name: characterData.name });
          } else {
            reject(error);
          }
        });
      }));
    });

    Promise.all(promises).then((results) => {
      results.forEach((result) => {
        console.log(`${result.index} - ${result.name}`);
      });
    }).catch((error) => {
      console.error('Error:', error);
    });
  } else {
    console.error('Error:', error);
  }
});
