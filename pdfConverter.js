
// window.jsPDF = window.jspdf.jsPDF;

// var doc = new jsPDF();
var doc = new jsPDF();
	
doc.text(20, 20, 'Hello world!');
doc.text(20, 30, 'This is client-side Javascript to generate a PDF.');

// Add new page
doc.addPage();
doc.text(20, 20, 'Visit CodexWorld.com');

// Save the PDF
doc.save('document.pdf');