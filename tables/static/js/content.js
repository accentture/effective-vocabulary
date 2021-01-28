

function addRows(){
    let tableContainer = document.querySelector('.table-container')
    console.log(tableContainer.innerHTML)
    const row = document.createElement('div')
    row.classList.add("row-content")
    let form = document.createElement('form')
    form.classList.add("form-words")
    form.method = 'POST'
    form.action = "/tabla/6"

    /* let field0 = document.createElement('span') */
    const field0 = document.createElement('input')
    field0.type = 'hidden'
    field0.name = 'csrfmiddlewaretoken'
    field0.value = 'HETwHypusDXpLV0tvNPwQQtcTAsyb7IX5xjRTH9vEgKBWXoJhUn0D5LwxYfcrWUm'
    const field1 = document.createElement('div')
    const field2 = document.createElement('div')
    const field3 = document.createElement('div')
    const field4 = document.createElement('div')
    

    const inputEnglish = document.createElement('input')
    inputEnglish.type = 'text'
    inputEnglish.name = 'english_word'

    const inputEspanish = document.createElement('input')
    inputEspanish.type = 'text'
    inputEspanish.name = 'spanish_word'

    const inverosimilRelation = document.createElement('input')
    inverosimilRelation.type = 'text'
    inverosimilRelation.name = 'inverosimil_relation'

    const buttonSave = document.createElement('input')
    buttonSave.type = 'submit'
    buttonSave.value = 'Enviar'



    
    field1.append(inputEnglish)
    field2.append(inputEspanish)
    field3.append(inverosimilRelation)
    field4.append(buttonSave)

    form.append(field0)
    form.append(field1)
    form.append(field2)
    form.append(field3)
    form.append(field4)
    

    row.append(form)

    tableContainer.append(row)
}


const buttonAddRow = document.querySelector('.button-add')
buttonAddRow.addEventListener('click', addRows)

