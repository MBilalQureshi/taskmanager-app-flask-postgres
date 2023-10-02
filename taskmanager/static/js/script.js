document.addEventListener('DOMContentLoaded', function () {
  //sidenav initialization  
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // Modals initialization
  let modals = document.querySelectorAll('.modal');
  M.Modal.init(modals);

  // datepicker initialization
  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    i18n: {
      done: "Select"
    }
  });

  // select initialization
  let select = document.querySelectorAll('select');
  M.FormSelect.init(select);
});
