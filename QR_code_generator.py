import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode
import os

# Generate QR code from file path
def generate_qr_from_path(path):
    qr = qrcode.make(path)
    qr_path = "image_path_qr.png"
    qr.save(qr_path)
    return qr_path

# Handle image selection
def select_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg *.gif")]
    )
    if file_path:
        # Display selected image
        show_selected_image(file_path)

        # Generate QR code from image path
        qr_path = generate_qr_from_path(file_path)
        show_qr_image(qr_path)

        # Store path for saving
        save_button.config(state="normal")
        save_button.qr_path = qr_path

# Display selected image
def show_selected_image(path):
    img = Image.open(path)
    img = img.resize((200, 200))
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo
    image_name_label.config(text=os.path.basename(path))

# Display QR code
def show_qr_image(path):
    qr = Image.open(path)
    qr = qr.resize((200, 200))
    qr_photo = ImageTk.PhotoImage(qr)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

# Save the QR code
def save_qr():
    path = filedialog.asksaveasfilename(
        defaultextension=".png", filetypes=[("PNG files", "*.png")]
    )
    if path:
        try:
            img = Image.open(save_button.qr_path)
            img.save(path)
            messagebox.showinfo("Saved", f"QR code saved as {path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# GUI Setup
window = tk.Tk()
window.title("QR Code from Image")
window.geometry("700x700")
window.resizable(False, False)

tk.Label(window, text="Select an Image to Generate QR", font=("Arial", 20, "bold")).pack(pady=10)

# Select Button
b1 = tk.Button(window, text="📁 Browse Image", font=("Arial", 20, "bold"), command=select_image)
b1.pack(pady=10)

# Selected Image Preview
image_name_label = tk.Label(window, text="", font=("Arial", 20, "bold"))
image_name_label.pack()

image_label = tk.Label(window)
image_label.pack(pady=5)

# QR Code Display
l1 = tk.Label(window, text="QR Code (from image path):", font=("Arial", 20, "bold"))
l1.pack(pady=10)
qr_label = tk.Label(window)
qr_label.pack(pady=5)

# Save Button
save_button = tk.Button(window, text="💾 Save QR Code",  font=("Arial", 20, "bold"), command=save_qr, state="disabled")
save_button.pack(pady=15)

window.mainloop()
