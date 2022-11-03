
// определение кнопки добавления
var button_add = document.querySelector( '.dynamic_fields .js-add' );
 
// ожидание клика на кнопку .add
button_add.addEventListener( "click", function () {
 // какие-то действия
}

// определение блока, содержащего элементы
var students = document.querySelector( '.dynamic_fields .students' );
 
// клонирование образцового элемента
var element = document.querySelector( '.example_student' ).cloneNode( true );
 
// добавление класса к клонированному элементу
element.classList.add( 'student' );
 
// удаление класса из клонированного элемента
element.classList.remove( 'example_student' );
 
// добавление нового элемента к списку
students.appendChild( element );