import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_invoice_pdf(number, customer, items, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Customize the invoice layout as needed
    c.drawString(72, 780, f"Order Number {number}")
    c.drawString(72, 760, f"Invoice for {customer}")

    # Add headers
    c.drawString(72, 740, "Item Name")
    c.drawString(200, 740, "Barcode")
    c.drawString(300, 740, "Quantity")
    c.drawString(400, 740, "Price")
    c.drawString(500, 740, "Total")
    total = 0
    # Iterate over items and display information
    y_position = 720  # Initial Y position
    for code,item in items.items():
        c.drawString(72, y_position, item[0])
        c.drawString(200, y_position, code)
        c.drawString(300, y_position, f"{item[1]}")
        c.drawString(400, y_position, f"${float(item[2]):.2f}")
        item_total = float(item[2])*float(item[1])
        c.drawString(500, y_position, f"${item_total:.2f}")
        total+=item_total
        y_position -= 20  # Move to the next line

    # Add total price
    c.drawString(300, y_position - 20, f"Total Price: ${total:.2f}")

    c.save()

def send_invoice_email(customer, email, pdf_filename):
    sender_email = 'lpsa732@gmail.com'  # Replace with your Gmail email address
    sender_password = 'dypn ibwj loiy xyxp'  # Replace with your Gmail password

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = f"Invoice for {customer}"

    # Attach the PDF invoice to the email
    with open(pdf_filename, 'rb') as attachment:
        pdf_part = MIMEApplication(attachment.read(), 'pdf')
        pdf_part.add_header('Content-Disposition', f'attachment; filename={pdf_filename}')
        message.attach(pdf_part)

    # Connect to the Gmail SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, email, message.as_string())

    print("Invoice email sent successfully")
