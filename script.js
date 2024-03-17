let selectedWord = "";

// Define the URL of the API endpoint you want to call
const apiUrl = "http://127.0.0.1:5000/api/get_random_word";

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
		selectedWord = data.answer.toLowerCase();

		// Manipulate the DOM to display the variable value
		document.getElementById("topic").textContent = data.topic;

		// Manipulate the DOM to display the variable value
		document.getElementById("hint").textContent = data.hint;

		setupInitialDisplay();
	})
	.catch((error) => {
		// Handle any errors that occur during the fetch operation
		console.error("There was a problem with the fetch operation:", error);
	});

// To store the already guessed letters
let guessedList = [];

// For initial display Word
let displayWord = "";

function setupInitialDisplay() {
	if (selectedWord.length > 0) {
		for (let i = 0; i < selectedWord.length; i++) {
			displayWord += "_ ";
		}

		document.getElementById("displayWord").textContent = displayWord.trimEnd();
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
	let letter = inputElement?.value?.toLowerCase();

	// To check empty input
	if (!letter) {
		alert("Empty Input box. Please add input letter");
		return;
	}

	// Clear the input field
	inputElement.value = "";
	shouldDisableSubmit();

	// Check if the letter has already been guessed
	if (guessedList.includes(letter)) {
		alert("You have already guessed that letter!");
		return;
	}

	// Add the letter to the guessed letters array
	guessedList.push(letter);

	// Update the word display based on the guessed letters
	let updatedDisplay = "";
	let allLettersGuessed = true;
	for (let i = 0; i < selectedWord.length; i++) {
		if (guessedList.includes(selectedWord[i])) {
			updatedDisplay += selectedWord[i] + " ";
		} else {
			updatedDisplay += "_ ";
			allLettersGuessed = false;
		}
	}
	document.getElementById("displayWord").textContent = updatedDisplay;

	// Check if all letters have been guessed
	if (allLettersGuessed) {
		document.getElementById("displayWord").className += "success";

		// Show success message
		setTimeout(() => {
			alert("Congratulations! You guessed the word correctly!");
		}, 1000);
	}
}
