/* =========================================================
   Valora / Wealth — lead form → Google Sheet + email alert
   Sheet columns: Name | Email | Phone Number | Solving For | Message
   ---------------------------------------------------------
   Deploy: Deploy ▸ New deployment ▸ Web app
           Execute as: Me
           Who has access: Anyone
           Copy the /exec URL into SHEET_ENDPOINT in script.js
   ========================================================= */

// Sheet ID only — NOT the full URL
var SHEET_ID  = '1vWxHqtLPMb_RqE0rTuTyHWh_PJ5o7RkHx5Jyy2P3QCg';
var SHEET_NAME = '';                         // '' = first sheet, or e.g. 'Leads'
var NOTIFY_TO  = 'barot@valorahq.com,brands@grow.surgeaio.com';
var HEADERS    = ['Name', 'Email', 'Phone Number', 'Solving For', 'Message'];

function doGet(e)  { return handleForm(e); }
function doPost(e) { return handleForm(e); }

function handleForm(e) {
  try {
    var params = (e && e.parameter) ? e.parameter : {};

    var name    = str(params.name);
    var email   = str(params.email);
    var phone   = str(params.phone);
    var solving = str(params.goal || params.solving || params.service);
    var message = str(params.note || params.message);

    if (!name || !email || !phone) {
      return json({ status: 'error', message: 'Missing required fields' });
    }

    var sheet = getSheet();

    // Write the header row only once, on an empty sheet
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(HEADERS);
      sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
      sheet.setFrozenRows(1);
    }

    sheet.appendRow([name, email, phone, solving, message]);
    SpreadsheetApp.flush();

    var timestamp = Utilities.formatDate(
      new Date(),
      Session.getScriptTimeZone(),
      'dd/MM/yyyy HH:mm:ss'
    );

    GmailApp.sendEmail(
      NOTIFY_TO,
      'Valora New Organic Lead - ' + name,
      'New Lead Received\n\n' +
      'Name: '         + name    + '\n' +
      'Email: '        + email   + '\n' +
      'Phone Number: ' + phone   + '\n' +
      'Solving For: '  + solving + '\n' +
      'Message: '      + (message || '-') + '\n' +
      'Time: '         + timestamp
    );

    return json({ status: 'success', message: 'Lead captured' });

  } catch (err) {
    return json({ status: 'error', message: err.toString() });
  }
}

/* ---------------- helpers ---------------- */

function getSheet() {
  var ss = SpreadsheetApp.openById(SHEET_ID);
  if (SHEET_NAME) {
    return ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
  }
  return ss.getSheets()[0];
}

function str(v) {
  return (v === null || v === undefined) ? '' : String(v).trim();
}

function json(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

/* ---------------- manual test ---------------- */

function testHandleForm() {
  var fakeEvent = {
    parameter: {
      name: 'Test User',
      email: 'test@example.com',
      phone: '9999999999',
      goal: 'Retirement income',
      note: 'Looking for a second opinion on my 401k.'
    }
  };
  Logger.log(handleForm(fakeEvent).getContent());
}
