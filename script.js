const bot = "Antriksh-";
const question = "Query-";
document.querySelector(".t1").addEventListener("click", function () {
  botMessage =
    "Welcome diverse learners click anywhere and just say log me in.";
  let message = new SpeechSynthesisUtterance(botMessage);
  window.speechSynthesis.speak(message);
});
document.querySelector(".bgm").addEventListener("click", function () {
  const texts = document.querySelector(".q");

  window.SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

  const recognition = new SpeechRecognition();
  recognition.interimResults = true;

  let p = document.createElement("p");

  recognition.addEventListener("result", (e) => {
    texts.appendChild(p);
    const text = Array.from(e.results)
      .map((result) => result[0])
      .map((result) => result.transcript)
      .join("");

    p.innerText = question + text;
    //  document.getElementById("j").innerHTML = text;

    if (e.results[0].isFinal) {
      if (text.includes("how are you")) {
        p = document.createElement("p");
        p.classList.add("replay");
        p.innerText = "I am fine";
        texts.appendChild(p);
      }
      if (text.includes("login")) {
        p = document.createElement("p");
        p.classList.add("replay");
        p.innerText = "opening bhuvan Adhaar";
        console.log("opening bhuvan Adhaar");
        window.open("login.html");
      }
      if (text.includes("show highlights")) {
        p = document.createElement("p");
        p.classList.add("replay");
        p.innerText = "showing highlights";
        console.log("show highlights");
        window.open("highlights.html");
      }
      if (text.includes("open nrsc")) {
        p = document.createElement("p");
        p.classList.add("replay");
        p.innerText = "opening NRSC website";
        console.log("opening NRSC website");
        window.open("https://bhuvan-app3.nrsc.gov.in/data/download/index.php");
      }
      if (text.includes("open Bhuvan 2D")) {
        p = document.createElement("p");
        p.classList.add("replay");
        p.innerText = "opening bhuvan 2D website";
        console.log("opening bhuvan 2D website");
        window.open(
          "https://bhuvan-app1.nrsc.gov.in/bhuvan2d/bhuvan/bhuvan2d.php"
        );
      }
      if (text.includes("open API")) {
        p = document.createElement("p");
        p.classList.add("replay");
        console.log("opening Bhuvan API");
        window.open("https://bhuvan-app1.nrsc.gov.in/api/");
      }
      if (text.includes("open Bhuvan tourism")) {
        p = document.createElement("p");
        p.classList.add("replay");
        console.log("opening bhuvan tourism");
        window.open("https://bhuvan-app1.nrsc.gov.in/tourism/tourism.php");
      }
      if (text.includes("open Bhuvan home page")) {
        p = document.createElement("p");
        p.classList.add("replay");
        console.log("opening bhuvan homepage");
        window.open("https://bhuvan.nrsc.gov.in/home/index.php");
      }
      if (text.includes("show your features")) {
        p = document.createElement("p");
        p.classList.add("replay");
        console.log("opening features page");
        window.open("features.html");
      } else {
        window.speechSynthesis.cancel();
        fetch("http://localhost:5005/webhooks/rest/webhook", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ message: text }),
        })
          .then((response) => response.json())
          .then((data) => {
            p = document.createElement("p");
            p.classList.add("replay");
            const botMessage = data[0]
              ? data[0].text
              : "No reply from the bot.";
            p.innerText = bot + botMessage;
            texts.appendChild(p);
            let message = new SpeechSynthesisUtterance(botMessage);
            window.speechSynthesis.speak(message);
          })
          .catch((error) => {
            console.error("Error:", error);
            p = document.createElement("p");
            p.classList.add("replay");
            p.innerText = "Error fetching response";
            texts.appendChild(p);
          });
      }
      p = document.createElement("p");
    }
  });

  recognition.addEventListener("end", () => {
    recognition.start();
  });

  recognition.start();
});
