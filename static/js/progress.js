$(document).ready(function() {

$( ".basic" ).click(function() {
	  waitingDialog.show('Loading Something...');
	setTimeout(function () {
	  waitingDialog.hide();
	}, 3000);
	});
$( ".government" ).click(function() {
		  waitingDialog.show('Rebilling Members...',{
			  headerText: 'ProgressTracker',
						dialogSize: 'sm',
						progressType: 'danger'
			  });
		setTimeout(function () {
		  waitingDialog.hide();
		}, 12000);
		});
$( ".callback" ).click(function() {
	  waitingDialog.show('Loading Something...',{
					progressType: 'success',
					onHide: function () {alert('Callback!');}
		  });
	setTimeout(function () {
	  waitingDialog.hide();
	}, 3000);
});

});