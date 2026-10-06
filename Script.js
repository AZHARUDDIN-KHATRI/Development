const quizData = [
    {
        question: "What does HTML stand for?",
        options: ["Hyper Text Markup Language", "High Text Markup Language", "Hyper Tabular Markup Language", "None of these"],
        correct: 0
    },
    {
        question: "Which language is used for web styling?",
        options: ["Python", "PHP", "CSS", "C++"],
        correct: 2
    },
    {
        question: "What is the default port for HTTP?",
        options: ["443", "80", "21", "8080"],
        correct: 1
    }
];

let currentIdx = 0;
let score = 0;

const questionEl = document.getElementById("question");
const optionsContainer = document.getElementById("options-container");
const nextBtn = document.getElementById("next-btn");
const resultBox = document.getElementById("result-box");
const quizBox = document.getElementById("quiz-box");
const scoreText = document.getElementById("score-text");
const restartBtn = document.getElementById("restart-btn");

function loadQuiz() {
    resetState();
    let currentQuiz = quizData[currentIdx];
    questionEl.innerText = `${currentIdx + 1}. ${currentQuiz.question}`;

    currentQuiz.options.forEach((option, idx) => {
        const button = document.createElement("button");
        button.innerText = option;
        button.classList.add("option-btn");
        button.addEventListener("click", () => selectOption(idx));
        optionsContainer.appendChild(button);
    });
}

function resetState() {
    optionsContainer.innerHTML = "";
}

function selectOption(selectedIdx) {
    if (selectedIdx === quizData[currentIdx].correct) {
        score++;
    }
    if (currentIdx < quizData.length - 1) {
        currentIdx++;
        loadQuiz();
    } else {
        showResults();
    }
}

function showResults() {
    quizBox.classList.add("hidden");
    resultBox.classList.remove("hidden");
    scoreText.innerText = `You scored ${score} out of ${quizData.length}!`;
}

restartBtn.addEventListener("click", () => {
    currentIdx = 0;
    score = 0;
    quizBox.classList.remove("hidden");
    resultBox.classList.add("hidden");
    loadQuiz();
});

loadQuiz();
