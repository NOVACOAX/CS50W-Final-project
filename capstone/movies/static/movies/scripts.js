$(document).ready( function () {
    $('#upcomingTable').DataTable();
} );
document.addEventListener('DOMContentLoaded', function() {

    // Search for content
    document.querySelector('#search_form').onsubmit = () => {
        div = document.querySelector('#res_content');
        div.innerHTML = `<div class="d-flex justify-content-center mt-5 mb-4">
                            <div class="loader"></div>
                        </div>`;
        // Get data
        Stext = document.querySelector('#searchText').value;
        Stype = document.querySelector('input[name="searchType"]:checked').value;

        // Send data
        fetch('search', {
            method: 'POST',
            body: JSON.stringify({
                text: Stext,
                type: Stype
        })
        })
        .then(response => response.json())
        .then(res => {
            if(res['result_count'] == 0){
                div.innerHTML = `<h3>No Results Found </h3>`;
            }else {
                count = res['result_count'];
                content = `<h3>Results | ${count}</h3>
                                <div class="row">`;
                for (re of res['results']) {
                    id = re['id'];
                    Iname = re['name'];
                    url = re['url'];
                    poster = re['poster'];
                    if(id.startsWith("tt")){
                        dir = `movie/${id}`;
                    }else{
                        dir = `people/name/${id}`;
                    }
                    item = `<div class="col-md-6 col-12 p-3">
                                <div class="media border border-warning rounded">
                                    <a href="/movies/${dir}"  class=" mr-2">
                                        <img src="${poster}" alt="Poster" class="rounded-left" style="width:70px;">
                                    </a>
                                    <div class="media-body">
                                        <h5 class="mt-0">${Iname}</h5>
                                        <a type="button" class="btn btn-warning mr-2 float-right" href="${url}">IMDB</a>
                                    </div>
                                </div>
                            </div>`;
                    content += item;
                    
                }
                content += `</div>`;

                div.innerHTML = content;
            }
        });

        // Stop form from submitting
        return false;
    }

    // Toggle search modal
    // Get the modal
    var modal = document.getElementById("Search_res_div");
    // Get the button that opens the modal
    var btn = document.getElementById("search_btn");
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
    // When the user clicks on the button, open the modal
    btn.onclick = function() {
        modal.style.display = "block";
    }
    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
})
// Add to watchlist
function enList(id){
    btn = document.querySelector('#Listbtn');
    fetch(`${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            listed: 'no'
        })
    })
    .then(response => {
        if(response.ok) {
            // Change th button
            btn.innerHTML = `<button type="button" class="btn btn-dark" onclick="unList('${id}')"><i  class='bx bx-minus'></i> Watchlist </button>`;
        }
    })
}
// Remove from watchlist
function unList(id){
    btn = document.querySelector('#Listbtn');
    fetch(`${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            listed: 'yes'
        })
    })
    .then(response => {
        if(response.ok) {
            // Change the btn
            btn.innerHTML = `<button type="button" class="btn btn-dark" onclick="enList('${id}')"><i  class='bx bx-plus'></i> Watchlist </button>`;
        }
    })
}
