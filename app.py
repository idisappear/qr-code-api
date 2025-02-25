from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/generate_qr')
def generate_qr():
    # Get payment details from URL parameters
    name = request.args.get('Name', 'Unknown')
    personal_acc = request.args.get('PersonalAcc', '00000000000000000000')
    bank_name = request.args.get('BankName', 'Unknown Bank')
    bic = request.args.get('BIC', '000000000')
    sum_ = request.args.get('Sum', '10000')  # Default to 100 RUB (in kopecks)
    purpose = request.args.get('Purpose', 'Оплата')
    payee_inn = request.args.get('PayeeINN', '0000000000')

    # Construct QR code data
    qr_data = (
        f"ST00012|"
        f"Name={name}|"
        f"PersonalAcc={personal_acc}|"
        f"BankName={bank_name}|"
        f"BIC={bic}|"
        f"Sum={sum_}|"
        f"Purpose={purpose}|"
        f"PayeeINN={payee_inn}"
    )

    # Generate QR code
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image in memory
    img_io = io.BytesIO()
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
