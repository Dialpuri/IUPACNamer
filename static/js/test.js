function checkButtonPressed() {
    var input = document.getElementById('guess')

    if (input.value == "") {
        alert("Please enter a valid guess :)")
    }

    console.log(input.value)
}