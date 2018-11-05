$(document).ready(function() {

$( ".basic" ).click(function() {
	  waitingDialog.show('Loading Something...');
	setTimeout(function () {
	  waitingDialog.hide();
	}, 3000);
	});
$( ".government" ).click(function() {
		  waitingDialog.show('Rebilling Government Members...',{
			  headerText: 'ProgressTracker',
						dialogSize: 'sm',
						progressType: 'success'
			  });
		setTimeout(function () {
		  waitingDialog.hide();
		}, 20000);
		});
$( ".commercial" ).click(function() {
		  waitingDialog.show('Rebilling Commercial Members...',{
			  headerText: 'ProgressTracker',
						dialogSize: 'sm',
						progressType: 'success'
			  });
		setTimeout(function () {
		  waitingDialog.hide();
		}, 20000);
		});
$( ".validate" ).click(function() {
		  waitingDialog.show('VALIDATING FILE...',{
			  headerText: 'ProgressTracker',
						dialogSize: 'sm',
						progressType: 'success'
			  });
		setTimeout(function () {
		  waitingDialog.hide();
		}, 60000);
		});
$( ".delete" ).click(function() {
		  waitingDialog.show('DELETING FILE...',{
			  headerText: 'ProgressTracker',
						dialogSize: 'sm',
						progressType: 'danger'
			  });
		setTimeout(function () {
		  waitingDialog.hide();
		}, 20000);
		});
$( ".etlcall" ).click(function() {
		  waitingDialog.show('CALLING ETL REALTIME...',{
			  headerText: 'ProgressTracker',
						dialogSize: 'sm',
						progressType: 'success'
			  });
		setTimeout(function () {
		  waitingDialog.hide();
		}, 60000);
		});
$( ".login" ).click(function() {
		  waitingDialog.show('VALIDATING YOUR ACCESS...',{
			  headerText: 'ProgressTracker',
						dialogSize: 'sm',
						progressType: 'success'
			  });
		setTimeout(function () {
		  waitingDialog.hide();
		}, 200000);
		});
$( ".singlemedicare" ).click(function() {
		  waitingDialog.show('SEARCHING DATA IN METAVANCE...',{
			  headerText: 'ProgressTracker',
						dialogSize: 'sm',
						progressType: 'success'
			  });
		setTimeout(function () {
		  waitingDialog.hide();
		}, 600000);
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