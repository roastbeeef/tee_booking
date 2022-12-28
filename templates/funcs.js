// function scrapeAvailability(url) {
//     // fetch
//     // jsonify
//     // iteratively create the string
//     function fetch_url_and_jsonify(url) {
//         return fetch(url).then(response).json()
//     };

//     function create_output_string(json_obj) {
//         let optionHTML = '';
            
//         for (let booking_time of json_obj.booking_times) {
//             optionHTML += '<option value="' + booking_time.id + '">' + booking_time.name + '</option>';
//         };

//         return optionHTML;
//     };
    
//     var json_obj = fetch_url_and_jsonify(url)
//     return create_output_string(json_obj);
// };
// test_url = 'http://127.0.0.1:5000/booking_time/2022-12-27'

// fetch(test_url).then(function(response) {
//     // this injects the HTML into the divs to show the options in the SelectField. impacts nothing cosmetically
    
//     response.json().then(function(data) {
//         let optionHTML = '';
        
//         for (let booking_time of data.booking_times) {
//             optionHTML += '<option value="' + booking_time.id + '">' + booking_time.name + '</option>';
//         };
//     });

// });

input_url = 'hello, world'

function hello_world(input_url) {
    return input_url
}

hello_world(input_url)