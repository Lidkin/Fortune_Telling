let uQuestion = '';

butrandom.addEventListener('click', randomQuote);
userquestion.addEventListener('input', getQuestion);
butbybook.addEventListener('click', getTytleBook);

const getQuestion = (event) => { uQuestion = event.target.value; };

async function getTytleBook() {
    try {
        const booksData = await fetch('http://localhost:8000/fortune/books/')
        if (booksData.ok) {
            const books = await booksData.json();
            booksForm(books);
        }
    } catch (err) {
        err;
    }
};

function booksForm(books) {
    const booksList = document.createElement('select');
    booksList.setAttribute('id', 'choice');
    books.forEach(book => {
        const option = document.createElement('option');
        option.setAttribute('value', book['book']);
        option.textContent = book['book'];
        booksList.appendChild(option);
    });

    bybook.innerHTML = `<label for="choice">Choose the book:</label>`
    bybook.appendChild(booksList);

    booksList.addEventListener('change', searchByBook);
};

async function searchByBook(event) {
    console.log(event.srcElement.value)
    try {
        const quoteData = await fetch(`http://localhost:8000/fortune/book/${event.srcElement.value}`)
        if (quoteData.ok) {
            const quote = await quoteData.json();
            console.log(quote)
            answer(quote);
        }
    } catch (err) {
        err
    }
};

function answer(quote, target = '') {

    const rundAnswer = document.createElement('p');
    if (target.id === 'butrandom') {
        rundAnswer.innerText = quote[0]['content'];
        random.appendChild(rundAnswer)
    } else {
        rundAnswer.innerText = quote;
        bybook.appendChild(rundAnswer)
    }
};

async function randomQuote(event) {
    const keys = await tags();
    const questionArr = uQuestion.toLowerCase().replace(/[^a-zA-Z\s]+/g, '').split(' ');
    console.log(questionArr);
    // postQuestion(questionArr);
    const commonElements = questionArr.map(word => keys.find(item => word == item));
    const category = commonElements.length > 0 ? commonElements.length > 1 ? commonElements.join('|') : commonElements.join('') : keys[questionArr.length < keys.length / 10 ? Math.floor(Math.random() * keys.length) : Math.floor(Math.random() * questionArr.length)]; // if user input not empty and his words containts in keys, then We need to check it's word or sentence. If it's sentence return string of words seperated | . If input not contains in keys we need to check length of keys and input user for randomaizing 
    try {
        const data = await fetch(`https://api.quotable.io/quotes/random?tags=${category}`);
        if (data.ok) {
            const quote = await data.json();
            answer(quote, event.target);
        } else {
            throw new Error;
        }

    } catch (err) {
        err;
    }
};

async function tags() {
    try {
        const data = await fetch('https://api.quotable.io/tags')
        if (data.ok) {
            const dataJson = await data.json();
            return dataJson.map(item => item['slug']);
        }
    } catch (error) {
        console.log(error);
    }
}

async function postQuestion(questionArr) {
    let question = questionArr.toSorted().join(' ');
    let newQuestion = { question };
    let options = {
        method: "POST",
        headers: {
            "Content-type": "application/json",
        },
        body: JSON.stringify(newQuestion),
    };
    try {
        const res = await fetch("http://localhost:8000/fortune/question", options);
        const data = await res.json();
        consolee.log(data);
    } catch (error) {
        console.log(error);
    }
}
