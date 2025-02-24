import qrcode

# Payment details in ST00012 format (Adjusted to match the reference QR)
payment_data = (
    "ST00012|"
    "Name=СНТ \"МАЯК\"|"
    "PersonalAcc=40703810700000015594|"
    "BankName=ФИЛИАЛ \"ЦЕНТРАЛЬНЫЙ\" БАНКА ВТБ (ПАО)|"
    "BIC=044525411|"
    # "CorrespAcc=30101810400000000411|"  # Correspondent Account
    "Sum=1500000|"  # Amount in kopecks (15000 RUB = 1500000 kopecks)
    "Purpose=Оплата за электроэнергию на общественную зону. 01 2025. Дом 18|"
    "PayeeINN=5017051411|"
    #"lastName=Виноградов|"
    #"firstName=Александр|"
    #"middleName=Александрович|"
    #"payerAddress=Москва, ул. Примерная, д. 10|"
    #"paymPeriod=012025|"  # Payment period in MMYYYY format
    #"TechCode=02|"  # Technical payment code
    #"persAcc=3013809920201|"  # Personal account number
    #"FIO=Виноградов Александр Александрович"
)

# Create a QR code object
qr = qrcode.QRCode(
    version=10,  # Increased version for more data capacity
    error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
    box_size=10,
    border=4,
)

# Add data and generate the QR code
qr.add_data(payment_data)
qr.make(fit=True)

# Create the QR code image
qr_image = qr.make_image(fill="black", back_color="white")

# Show and save the QR code
qr_image.show()
qr_image.save("payment_qr_st00012_fixed.png")

print("ST00012 QR code generated and saved as 'payment_qr_st00012_fixed.png'.")
