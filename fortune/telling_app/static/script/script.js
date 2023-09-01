Authenticator:
//
// const loginForm = document.createElement('form');
// loginForm.innerHTML = `<label for='username'>User Name:</label><br>
// <input name='username' type='text' /><br>
// <label for='password'>Password:</label><br>
// <input name='password' type='password' /><br>
// <button id='subbut'>Login</button>`
//
// formlogin.appendChild(loginForm);
//
// loginForm.addEventListener('submit', postToDB);
//
//
// async function postToDB(event) {
// event.preventDefault();
// const username = event.target.username.value;
// const password = event.target.password.value;
//
// loginForm({ username, password });
// };
//
// async function loginForm(userData) {
//
// let options = {
// method: "POST",
// headers: {
// "Content-type": "application/json",
// },
// body: JSON.stringify({ userData }),
// };
// try {
// const postTo = await fetch("http://localhost:8000/autorization/login/", options); //replace with the corresponding link
// if (postTo.ok) {
// //going to main page
// } else {
// throw Error;
// }
// } catch (e) {
// console.log(e);
// }
//
//
// };
//

// var quotes = require('random-movie-quotes')

// console.log(quotes.getQuote())


bybook.addEventListener('click', getTytleBook)

async function getTytleBook() {
    try {
        const booksData = await fetch('http://127.0.0.1:8000/fortune-telling/books/', { mode: 'no-cors' }) //replace with the corresponding link
        if (booksData.ok) {
            const books = await booksData.json();
            console.log(books)
            booksForm(books);
        }
    } catch (err) {
        err;
    }
}

function booksForm(books) {
    const booksList = document.createElement('select');
    booksList.id = 'choice';
    books['book'].forEach(book => {
        booksList.innerHTML = `<option name='choice'>${book[tytle]}</option>`
    });

    bybook.innerHTML = `<label for="choice">Choose the book:</label>`
    bybook.appendChild(booksList);

    booksList.addEventListener('select', searchByBook)
}

async function searchByBook(event) {

    try {
        const quoteData = await fetch(`http://127.0.0.1:8000/fortune-telling/fortune-telling/book/${event.target.value}`, { mode: 'no-cors' })
        if (quoteData.ok) {
            const quote = await quoteData.json();
            answer(quote);
        }
    } catch (err) {
        err
    }
}

function answer(quote) {
    const rundAnswer = document.createElement('p');
    rundAnswer.innerText = quote;
}

// console.log((randomQuotes())())
