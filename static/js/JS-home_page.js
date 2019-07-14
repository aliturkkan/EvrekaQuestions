window.onload = function() {
    var date_input=$('input[name="date-picker"]');
    var container=$('.date-info form').length>0 ? $('.date-info form').parent() : "body";
    var options={
        format: 'mm.dd.yyyy',
        container: container,
        todayHighlight: true,
        autoclose: true,
    };
    date_input.datepicker(options);
};