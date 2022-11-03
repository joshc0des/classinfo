$(document).ready(function () {
    $('#table1').DataTable({
        ajax: 'data/datatablesdata.txt',
        columns: [
            { title: 'Index' },
            { title: 'CRN' },
            { title: 'Subject' },
            { title: 'Course' },
            { title: 'Section' },
            { title: 'Section Title' },
            { title: 'Primary Instructor' },
            { title: 'Course Dates' },
            { title: 'Seats Left' },
            { title: 'Wait List' }
        ]
    });
})