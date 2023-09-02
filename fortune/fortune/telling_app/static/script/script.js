const keyList = ['age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'best', 'birthday', 'business',
    'carchange', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'dreams', 'education',
    'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fear', 'fitness', 'food', 'forgiveness',
    'freedom', 'friendship', 'funny', 'future', 'god', 'good', 'government', 'graduation', 'reat', 'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy', 'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'medical', 'men', 'mom', 'money', 'morning', 'movies', 'success'];
let question = '';

const getQuestion = (event) => { question = event.target.value; };

butrandom.addEventListener('click', randomQuote);
userquestion.addEventListener('input', getQuestion);

butbybook.addEventListener('click', getTytleBook);

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
    const questionArr = question.toLowerCase().replace(/[^a-zA-Z\s]+/g, '').split(' ');
    const firstCommonElement = keyList.find(item => questionArr.includes(item));
    const category = firstCommonElement != undefined ? firstCommonElement : keyList[keyList.length - questionArr.length];
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