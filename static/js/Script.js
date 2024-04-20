const signup = document.getElementById('signup');
const editar_user = document.getElementById('editar_user');
const inputs = document.querySelectorAll('#signup input', '#editar_user input');



const expresiones = {
  nombre: /^[a-zA-ZÀ-ÿ\s]{5,40}$/, // Letras y espacios, pueden llevar acentos.
  correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
  telefono: /^\d{10}$/, // 10 digitos
  documento: /^\d{8,10}$/ // 8-10 digitos
}

// Validando formulario de registro

const campos = {
  user_name: false,
  user_email: false,
  user_phone: false,
  user_doc: false
}

const validarFormulario = (e) => {

  switch (e.target.name) {

    case "user_name":
      if (expresiones.nombre.test(e.target.value)) {
        document.getElementById('user_name').classList.remove('formulario-incorrecto');
        document.getElementById('user_name').classList.add('formulario-correcto');
        campos['user_name'] = true;
      } else {
        document.getElementById('user_name').classList.add('formulario-incorrecto');
        campos['user_name'] = false;
      }
      break;

    case "user_email":
      if (expresiones.correo.test(e.target.value)) {
        document.getElementById('user_email').classList.remove('formulario-incorrecto');
        document.getElementById('user_email').classList.add('formulario-correcto');
        campos['user_email'] = true;

      } else {
        document.getElementById('user_email').classList.add('formulario-incorrecto');
        campos['user_email'] = false;

      }
      break;
    case "user_phone":
      if (expresiones.telefono.test(e.target.value)) {
        document.getElementById('user_phone').classList.remove('formulario-incorrecto');
        document.getElementById('user_phone').classList.add('formulario-correcto');
        campos['user_phone'] = true;

      } else {
        document.getElementById('user_phone').classList.add('formulario-incorrecto');
        campos['user_phone'] = false;

      }
      break;
    case "user_doc":
      if (expresiones.documento.test(e.target.value)) {
        document.getElementById('user_doc').classList.remove('formulario-incorrecto');
        document.getElementById('user_doc').classList.add('formulario-correcto');
        campos['user_doc'] = true;

      } else {
        document.getElementById('user_doc').classList.add('formulario-incorrecto');
        campos['user_doc'] = false;

      }
      break;
  }
};


inputs.forEach((input) => {

  input.addEventListener('keyup', validarFormulario);
  input.addEventListener('blur', validarFormulario);

});

signup.addEventListener('submit', (e) => {

  if (campos.user_name && campos.user_email && campos.user_phone && campos.user_doc) {
    signup.reset();
    alert("El Cliente se registro de manera exitosa");
  }
  else {
    e.preventDefault();
    alert("Verifica los datos");
  }
});

editar_user.addEventListener('submit', (e) => {

  if (campos.user_name && campos.user_email && campos.user_phone && campos.user_doc) {
    editar_user.reset();
    alert("El Cliente se registro de manera exitosa");
  }
  else {
    e.preventDefault();
    alert("Verifica los datos");
  }
});


// Validar editar

// const camposE = {
//   user_name: false,
//   user_email: false,
//   user_phone: false,
//   user_doc: false
// }


// const validarFormularioEditar = (e) => {

//   switch (e.target.name) {

//     case "user_name":
//       if (expresiones.nombre.test(e.target.value)) {
//         document.getElementById('user_name').classList.remove('formulario-incorrecto');
//         document.getElementById('user_name').classList.add('formulario-correcto');
//         camposE['user_name'] = true;
//       } else {
//         document.getElementById('user_name').classList.add('formulario-incorrecto');
//         camposE['user_name'] = false;
//       }
//       break;

//     case "user_email":
//       if (expresiones.correo.test(e.target.value)) {
//         document.getElementById('user_email').classList.remove('formulario-incorrecto');
//         document.getElementById('user_email').classList.add('formulario-correcto');
//         camposE['user_email'] = true;

//       } else {
//         document.getElementById('user_email').classList.add('formulario-incorrecto');
//         camposE['user_email'] = false;

//       }
//       break;
//     case "user_phone":
//       if (expresiones.telefono.test(e.target.value)) {
//         document.getElementById('user_phone').classList.remove('formulario-incorrecto');
//         document.getElementById('user_phone').classList.add('formulario-correcto');
//         camposE['user_phone'] = true;

//       } else {
//         document.getElementById('user_phone').classList.add('formulario-incorrecto');
//         camposE['user_phone'] = false;

//       }
//       break;
//     case "user_doc":
//       if (expresiones.documento.test(e.target.value)) {
//         document.getElementById('user_doc').classList.remove('formulario-incorrecto');
//         document.getElementById('user_doc').classList.add('formulario-correcto');
//         camposE['user_doc'] = true;

//       } else {
//         document.getElementById('user_doc').classList.add('formulario-incorrecto');
//         camposE['user_doc'] = false;

//       }
//       break;
//   }
// };


// inputs.forEach((input) => {

//   input.addEventListener('keyup', validarFormulario);
//   input.addEventListener('blur', validarFormulario);

// });




// (function () {

//   $signup.addEventListener('submit', function (e) {

//     let user_name = String($user_name.value).trim();
//     if (user_name.length === 0) {
//       alert("El nombre de usuario no puede estar vacio");
//       e.preventDefault();
//     }
//   });

// })();