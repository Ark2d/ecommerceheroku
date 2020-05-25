$(document).ready(function(){
   $('.date-mask').mask('00/00/0000');
   $('.date-mask-placeholder').mask('00/00/0000', {placeholder: "Ex: 00 / 00/ 0000"});
   $('.phone-mask').mask('(00) 0000-0000');
   $('.cpf-mask').mask('000.000.000-00');
   $('.datepicker').datepicker({
       dateFormat: "dd/mm/yyyy",
   }).attr("autocomplete", "off");
});