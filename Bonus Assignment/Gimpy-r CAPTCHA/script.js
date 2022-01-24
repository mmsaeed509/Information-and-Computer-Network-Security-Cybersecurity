const captcha = document.querySelector(".captcha"),
reloadBtn = document.querySelector(".reload-btn"),
inputField = document.querySelector(".input-area input"),
checkBtn = document.querySelector(".check-btn"),
statusTxt = document.querySelector(".status-text");

//storing all captcha characters in array
let allCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
                     'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
function getCaptcha(){
  //getting 6 random characters from the array
  for (let i = 0; i < 6; i++) { 
    let randomCharacter = allCharacters[Math.floor(Math.random() * allCharacters.length)];
    //passing 6 random characters inside captcha innerText
    captcha.innerText += ` ${randomCharacter}`; 
  }
}
//calling getCaptcha when the page open
getCaptcha(); 
//calling getCaptcha & removeContent on the reload btn click
reloadBtn.addEventListener("click", ()=>{
  removeContent();
  getCaptcha();
});

url = "https://github.com/mmsaeed509";

checkBtn.addEventListener("click", e =>{
  //preventing button from it's default behaviour
  e.preventDefault(); 
  statusTxt.style.display = "block";
  //adding space after each character of user entered values because I've added spaces while generating captcha
  let inputVal = inputField.value.split('').join(' ');
  //if captcha matched
  if(inputVal == captcha.innerText){ 
    statusTxt.style.color = "#bc08c2";

    statusTxt.innerText = "You will go to Ozil's GitHub after 4 seconds.";
    //goto Ozil's GitHub after 4 seconds
    setTimeout(()=>{ 
      removeContent();
      window.location = url;
    }, 2000);
  }else{
    statusTxt.style.color = "#ff0000";
    statusTxt.innerText = "Captcha not matched. Please try again!";
  }
});

function removeContent(){
 inputField.value = "";
 captcha.innerText = "";
 statusTxt.style.display = "none";
}
