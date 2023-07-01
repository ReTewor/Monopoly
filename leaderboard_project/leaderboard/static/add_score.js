// add_score.js
//function addScoreToLeaderboard(score) {
window.addScoreToLeaderboard = function(score,result){
  var playerName = result;
  var playerScore = score;

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/add_score/", true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      console.log("Данные успешно отправлены");
    }
  };
  var data = JSON.stringify({ name: playerName, score: playerScore });
  xhr.send(data);
}