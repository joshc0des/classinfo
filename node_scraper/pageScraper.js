const fs = require('fs');
const scraperObject = {
	url: 'https://classnav.ou.edu/#semester/202220',
	async scraper(browser){
        let page = await browser.newPage();
        console.log(`Navigating to ${this.url}...`);
        // Navigate to the selected page
        await page.goto(this.url);

        function delay(time) {
            return new Promise(function(resolve) {
                setTimeout(resolve, time)
            });
        }

        var pages_data = {}; // Construct the main object for all course data
        pages_data['pages'] = []


        // Main Loop - through all pages
        for (var page_index = 0; page_index < 407; page_index++){
            // Click next page button after first loop iteration
            if (page_index >= 1){
                await page.click('#clist_next');
            }

            console.log(`loading page ${page_index + 1}`);
            await delay(10000); // Wait for page to fully load
            console.log(`page ${page_index + 1} loaded\n`);

            var names = await page.evaluate(() => { // Set text from all table cells to an array
                return Array.from(document.querySelectorAll("#clist > tbody > tr > td")).map(x => x.textContent)
            })


            var page_dict = {}; // Construct the object for a specific page of courses
            page_key = ("page_" + (page_index + 1).toString());
            page_dict[page_key] = [];
            pages_data["pages"].push(page_dict);

            for (var row_index = 0; row_index < names.length/10; row_index++){ // Loop through each row of the page cells
                var course_dict = {};

                var place_index = 0; // Temp place in a row
                for (var cell_index = row_index*10; cell_index < (row_index*10 + 10); cell_index++){ // Loop through each cell per row and add to the dictionary
                    switch (place_index) {
                        case 0:
                            course_dict["current_row_on_page"] = names[cell_index];
                                break;
                        case 1:
                            course_dict["crn"] = names[cell_index];
                                break;
                        case 2:
                            course_dict["subject"] = names[cell_index];
                            break;
                        case 3:
                            course_dict["course"] = names[cell_index];
                            break;
                        case 4:
                            course_dict["section"] = names[cell_index];
                            break;
                        case 5:
                            course_dict["section_title"] = names[cell_index];
                            break;
                        case 6:
                            course_dict["primary_instructor"] = names[cell_index];
                            break;
                        case 7:
                            course_dict["course_dates"] = names[cell_index];
                            break;
                        case 8:
                            course_dict["seats_left"] = names[cell_index];
                            break;
                        case 9:
                            course_dict["wait_list"] = names[cell_index];
                            break;
                    }
                    place_index++;
                }
                page_dict[page_key].push(course_dict);
            }
        }

        var jsonData = JSON.stringify(pages_data, null, 4);
        // console.log(jsonData);

        fs.writeFile("output.json", jsonData, 'utf8', function (err) {
        if (err) {
            console.log("An error occured while writing JSON Object to File.");
            return console.log(err);
        }

        console.log("JSON file has been saved.");
        })

        await browser.close()
    }
}

module.exports = scraperObject;
