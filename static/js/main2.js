console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreTopass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="text-right">والآن عزيزي الطالب … أجب عن أسئلة الاختبار القبلي التالي اذا حصلت على 85% فاكثر ستنتقل الى دراسة المديول الثانى ، وإذا حصلت على   أقل من 85% فابدأ في دراسة الموديول الحالي <b></b></div>
        <div class="h7 mb-3"><p class="text-right"><b>${name}? أختبار</b>"</p></div>
        <div class="text-right" >
            <ul>
                <li ><b>${difficulty} </b>:نوع الاختبار</li>
                <li ><b>${numQuestions} </b>:عدد الأسئلة</li>
                <li ><b>${scoreTopass}% </b>:المجموع </li>
                <li ><b>${time} min</b>:مدة الاختبار</li>
            </ul>
        </div>
`
    startBtn.addEventListener('click',()=>{
    window.location.href = url + pk
    })
}))