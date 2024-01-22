let hobbies = ["writing", "reading", "gardening", "crocheting", "listeningMusic"];

console.log(hobbies);

function addHobby(newHobby){
  hobbies.push(newHobby);
}

addHobby("cooking");
console.log(hobbies);

if (hobbies.length > 5){
  hobbies.shift();
}
console.log(hobbies);

for(let i=0; i<5; i++){
  console.log("My hobby " + (i+1) + ":" + hobbies[i] );
}





