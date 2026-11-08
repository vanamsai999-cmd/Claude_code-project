// Export MST-Study-Guide.html to PDF with every solution expanded.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.emulateMedia({ media: 'print', colorScheme: 'light' });
  await p.goto('file://' + path.join(__dirname, 'MST-Study-Guide.html'));
  await p.evaluate(() => document.querySelectorAll('details').forEach(d => d.open = true));
  await p.pdf({ path: path.join(__dirname, 'MST-Study-Guide.pdf'), format: 'A4', printBackground: true,
    margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' },
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#666">MATH6310 Study Guide · <span class="pageNumber"></span>/<span class="totalPages"></span></div>' });
  await b.close();
})();
