function uploadCSV() {
    const fileInput = document.getElementById('csvFile');
    const file = fileInput.files[0];
    var formData = new FormData();
    formData.append('file', file);
    console.log('Hi Java')

    var fileSubmittedUrl = "{{ url_for('fileSubmitted') }}";

    $.ajax({
        url: 'http://127.0.0.1:5000/fileSubmitted',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        // success: function (data) {

        //     console.log('data receied')
        //     console.log(data)
        //     window.location.replace('details.html')


        //     // document.getElementById("getSheetsButton").style.visibility = "visible";
        //     // document.getElementById("getSheetsButton").addEventListener("click", getSelectedSheetsColumns);
        //     // var sheetDiv = document.getElementById("listOfSheets");
        //     // for (item of data) {
        //     //     var a = document.createElement("a");
        //     //     a.addEventListener("click", aSelected);
        //     //     a.appendChild(document.createTextNode(item));
        //     //     // a.innerText = item;
        //     //     sheetDiv.appendChild(a);
        //     // }
        // },
        // error: function (error) {
        //     console.log("Error data back");
        // }
    });

}

