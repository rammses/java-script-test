    $(document).ready(function () {
      const endPoint = "https://localhost:5000/sessions";
      $('#doSomething').click(function () {
        fetch(endPoint)
          .then(data => {
            return data.json()
          })
          .then(res => {
            console.log(res)
            $('.message-body').append(JSON.stringify(res.data));
          })
      });
    });

