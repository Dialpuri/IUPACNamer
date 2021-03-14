var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

$(document).ready(function() { 

    var easy = document.getElementById('easy')
    var medium = document.getElementById('medium')
    var hard = document.getElementById('hard')
    var insane = document.getElementById('insane')

    easy.addEventListener('click', function() {
        $.post('/debug', {
            easy: "true"
        }).done(function(){
            window.location.reload();
            return false;
        })
    });

    medium.addEventListener('click', function() {
        $.post('/debug', {
            medium: "true"
        }).done(function(){
            window.location.reload();
            return false;
        })
    });

    hard.addEventListener('click', function() {
        $.post('/debug', {
            hard: "true"
        }).done(function(){
            window.location.reload();
            return false;
        })
    });

    insane.addEventListener('click', function() {
        $.post('/debug', {
            insane: "true"
        }).done(function(){
            window.location.reload();
            return false;
        })
    });
})

/*$(document).ready(function() {
    console.log("Document Ready")
    var guessSubmit = document.getElementById('guessSubmit')
    var guessInput = document.getElementById('guessInput')
    guessSubmit.addEventListener('click', function(){
        $.ajax({
            type: "POST",
            url: "/guess",
            data: {userGuess: guessInput.value},
            dataType: "text",
            complete: function(serverResponse){
                completionHandler(serverResponse);
            },
            error: function(error){
                errorHandler(error)
            }
        })
    }, false);
})*/

function completionHandler(serverResponse){
    isCorrect = JSON.parse(serverResponse.responseText).isCorrect;
    if (isCorrect) {
        console.log("TRUE");
        document.getElementById('container').style.color = 'orange';
    }
    else {
        console.log("FALSE");
        document.getElementById('container').style.color = 'green';
    }
}

function errorHandler(error){
    console.log(error);
}