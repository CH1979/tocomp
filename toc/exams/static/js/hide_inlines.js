window.addEventListener('load', function () {
  let answerType = document.getElementById('id_answer_type')
  let choiceLabels = document.getElementById('labelsforanswerchoice_set-group')
  let show_hide_div = function() {
    console.log(answerType.value)
    if (choiceLabels) {
      if (answerType.value=='SC' || answerType.value=='MC') {
        choiceLabels.style.display = 'block'
      } else {
        choiceLabels.style.display = 'none'
      }
    }
  }
  show_hide_div()
  answerType.onchange = function() {
    show_hide_div()
  }
})