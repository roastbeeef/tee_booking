		// this is to inject the HTML to update the tee times
		// if json is null then NO BOOKING TIMES AVAILABLE

		// other vars
		let booking_date_selection = document.getElementById('booking_date');
		let booking_time_selection = document.getElementById('booking_time');
		let booking_time_field = document.getElementById('booking_time_field');
		let booking_form_class = document.getElementById('booking_form_class');

		async function getBookingData(booking_date_str) {
			const response = await fetch(`/booking_time/${booking_date_str}`);	
			const data = await response.json();

			let optionHTML = '';
			for (let booking_time of data.booking_times) {
				optionHTML += `<option value="${booking_time.id}">${booking_time.name}</option>`;
			}

			return {
				booking_times: data.booking_times,
				booking_time_options: optionHTML
			};
		}


		// this populates the SelectField on page load - convert to async later
		window.onload = async function () {
			const booking_date_str = booking_date_selection.value; // this should come from python, but wont work via Jinja2
			const bookingData = await getBookingData(booking_date_str);
			let booking_times_count = bookingData.booking_times.length;
			booking_time_selection.innerHTML = bookingData.booking_time_options;
			
			// var tee_times_unavailable = (booking_times_count == 0)
			var tee_times_available = (booking_times_count != 0)

			if (tee_times_available) {
				document.getElementById('test_field').style = "display: none;";
				booking_time_field.style = "";
				booking_form_class.className = "alert alert-success";
			} else {
				document.getElementById('test_field').style = ""
				booking_time_field.style = "display: none;";
				booking_form_class.className = "alert alert-danger";
			}
			
		};

		// this populates the SelectField on update of the DateField
		booking_date_selection.onchange = async function () {
			const booking_date_str = booking_date_selection.value; // this should come from python, but wont work via Jinja2
			const bookingData = await getBookingData(booking_date_str);
			let booking_times_count = bookingData.booking_times.length;
			booking_time_selection.innerHTML = bookingData.booking_time_options;

			// var tee_times_unavailable = (booking_times_count == 0)
			var tee_times_available = (booking_times_count != 0)

			if (tee_times_available) {
				document.getElementById('test_field').style = "display: none;";
				booking_time_field.style = "";
				booking_form_class.className = "alert alert-success";
			} else {
				document.getElementById('test_field').style = ""
				booking_time_field.style = "display: none;";
				booking_form_class.className = "alert alert-danger";
			}
		};
