$(function () {
  var input = document.getElementById('searchTextField');
  var autocomplete = new google.maps.places.Autocomplete(input);
  autocomplete.addListener('place_changed', fillInAddress);

  function fillInAddress() {
    var place = autocomplete.getPlace().address_components;
    var formField = ""
    if (place != undefined) {
      for (var i = 0; i < place.length; i++) {
        switch (place[i].types[0]) {
          case 'route':
            formField = "calle";
            break;
          case 'locality':
            formField = "provincia";
            break;
          case 'postal_code':
            formField = "codigo_postal";
            break;
          case 'country':
            formField = "pais";
            break;
        }
        if (document.getElementById("id_" + formField)) {
          document.getElementById("id_" + formField).value = place[i].long_name;
        }
      }
    }
  }
});