# Convert excel file through Google Spreadsheets
import ezsheets

ss = ezsheets.upload('')    # Fill with excel file name

#ss.downloadAsExcel()
ss.downloadAsODS()
ss.downloadAsCSV()
ss.downloadAsTSV()
ss.downloadAsPDF()
ss.downloadAsHTML()
