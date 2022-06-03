console.log("Hello World");


$.ajax({
    url: '/api/v1/posts/',
    type: 'GET',
    success: function(response) {
        console.log(response);
    },
    error: function(response) {
    },
});