let selectedWord = "";

// Define the URL of the API endpoint you want to call
const apiUrl = "http://127.0.0.1:5000/api/word";
try {
  // Make a GET request to the API endpoint
  fetch(apiUrl)
    .then((response) => {
      // Check if the response is successful (status code 200)
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      // Parse the JSON response
      return response.json();
    })
    .then((data) => {
      // Handle the data received from the API
      selectedWord = data.answer;

      // Manipulate the DOM to display the variable value
      document.getElementById("topic").textContent = data.topic;

      // Manipulate the DOM to display the variable value
      document.getElementById("hint").textContent = data.hint;

      setupInitialDisplay();
    })
    .catch((error) => console.error("Error:", error));
} catch (error) {
  // Handle unexpected errors here
  console.error("Unexpected error occurred:", error);
}

// To store the already guessed letters
let guessedList = [];

// For initial display Word
let displayWord = "";

function setupInitialDisplay() {
  if (selectedWord.length > 0) {
    for (let i = 0; i < selectedWord.length; i++) {
      displayWord += "_ ";
    }

    document.getElementById("displayWord").className = "";
    document.getElementById("displayWord").textContent = displayWord.trimEnd();
    document.getElementById("letter-input").value = "";
    document.getElementById("letter-input").removeAttribute("disabled");
    document.getElementById("letter-input").focus();
  }
}

// Function to check if submit button should be enabled
function shouldDisableSubmit() {
  let inputElement = document.getElementById("letter-input");
  let letter = inputElement?.value?.toLowerCase();
  let disabled = false;

  if (!letter || !selectedWord) {
    disabled = true;
    inputElement.focus();
  }

  let guessBtnElement = document.getElementById("guess-btn");
  guessBtnElement.disabled = disabled;

  return disabled;
}

// Function to check Guessed letter
function guessLetter() {
  let inputElement = document.getElementById("letter-input");
  inputElement.setAttribute("disabled", true);
  let letter = inputElement?.value?.toLowerCase();

  // To check empty input
  if (!letter) {
    alert("Empty Input box. Please add input letter");
    inputElement.focus();
    return;
  }

  // Clear the input field
  inputElement.value = "";
  shouldDisableSubmit();

  let guessIndicator = document.getElementById("guess-result");

  const resetGuessMark = () => {
    setTimeout(() => {
      guessIndicator.innerHTML = "";
      inputElement.focus();
    }, 500);
  };

  // Check if the letter has already been guessed
  if (guessedList.includes(letter)) {
    guessIndicator.innerHTML = "&#x274c;";
    alert("You have already guessed that letter!");
    inputElement.removeAttribute("disabled");
    resetGuessMark();
    return;
  }

  // Add the letter to the guessed letters array
  guessedList.push(letter);

  // Update the word display based on the guessed letters
  let updatedDisplay = "";
  let allLettersGuessed = true;
  for (let i = 0; i < selectedWord.length; i++) {
    if (guessedList.includes(selectedWord[i].toLowerCase())) {
      updatedDisplay += selectedWord[i] + " ";
    } else {
      updatedDisplay += "_ ";
      allLettersGuessed = false;
    }
  }

  if (selectedWord.toLowerCase().includes(letter)) {
    guessIndicator.innerHTML = "&#10003;";
  } else {
    guessIndicator.innerHTML = "&#x274c;";
  }

  document.getElementById("displayWord").textContent = updatedDisplay;
  resetGuessMark();

  // Check if all letters have been guessed
  if (allLettersGuessed) {
    document.getElementById("displayWord").className += "success";
    inputElement.setAttribute("disabled", true);

    // Show success message
    setTimeout(() => {
      alert("Congratulations! You guessed the word correctly!");

      // Start a new game
      location.reload();
    }, 1000);
  } else {
    inputElement.removeAttribute("disabled");
  }
}
