import glob
import os
import random
import tkinter as tk

from PIL import Image, ImageTk


class PhotoGallery:
    def __init__(self, root):
        self.root = root
        self.pics_folder = "pics"

        # Configure window
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.attributes('-topmost', False)

        # Variables for dragging
        self.start_x = 0
        self.start_y = 0
        self.dragging = False
        self.resizing = False
        self.resize_corner = None

        # Store current image for resizing
        self.current_image = None
        self.current_image_path = None
        self.rotation_angle = 0  # Track rotation angle (0, 90, 180, 270)

        # Load and display image
        self.load_random_image()

        # Bind events
        self.root.bind('<Button-1>', self.start_drag)
        self.root.bind('<B1-Motion>', self.on_drag)
        self.root.bind('<ButtonRelease-1>', self.stop_drag)
        self.root.bind('<Escape>', self.exit_app)
        self.root.bind('<Key-r>', self.rotate_image)
        self.root.bind('<Key-R>', self.rotate_image)
        self.root.focus_set()  # Allow window to receive keyboard events

        # Bind resize events on borders
        self.setup_resize_bindings()

    def get_image_files(self):
        """Get all jpg and png files from pics folder"""
        if not os.path.exists(self.pics_folder):
            return []

        extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
        image_files = []
        for ext in extensions:
            image_files.extend(glob.glob(os.path.join(self.pics_folder, ext)))

        return image_files

    def load_random_image(self):
        """Load and display a random image"""
        image_files = self.get_image_files()

        if not image_files:
            # No images found, create a placeholder
            self.create_placeholder()
            return

        # Select random image
        image_path = random.choice(image_files)

        try:
            # Load image
            img = Image.open(image_path)

            # Store original image for resizing and rotation
            self.current_image = img.copy()
            self.current_image_path = image_path
            self.rotation_angle = 0  # Reset rotation when loading new image

            # Display the image with current rotation
            self.display_image()

        except Exception as e:
            print(f"Error loading image: {e}")
            self.create_placeholder()

    def display_image(self):
        """Display the current image with rotation applied"""
        if self.current_image is None:
            return

        try:
            # Get screen dimensions
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            # Apply rotation to the image
            img = self.current_image.copy()
            if self.rotation_angle != 0:
                img = img.rotate(-self.rotation_angle, expand=True)

            # Calculate size to fit screen (max 80% of screen)
            max_width = int(screen_width * 0.8)
            max_height = int(screen_height * 0.8)

            # Resize if needed while maintaining aspect ratio
            img_width, img_height = img.size
            ratio = min(max_width / img_width, max_height / img_height, 1.0)

            if ratio < 1.0:
                new_width = int(img_width * ratio)
                new_height = int(img_height * ratio)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Convert to PhotoImage
            self.photo = ImageTk.PhotoImage(img)

            # Update window size
            self.root.geometry(f"{img.width}x{img.height}")

            # Center window on screen
            x = (screen_width - img.width) // 2
            y = (screen_height - img.height) // 2
            self.root.geometry(f"{img.width}x{img.height}+{x}+{y}")

            # Create or update label with image
            if hasattr(self, 'label'):
                self.label.configure(image=self.photo)
            else:
                self.label = tk.Label(self.root, image=self.photo, bg='black')
                self.label.pack(fill=tk.BOTH, expand=True)
                # Add thin border
                self.root.configure(bg='#333333')
                self.label.configure(borderwidth=2, relief='solid', highlightthickness=1, highlightbackground='#333333')

        except Exception as e:
            print(f"Error displaying image: {e}")

    def rotate_image(self, event=None):
        """Rotate the current image by 90 degrees clockwise"""
        if self.current_image is None:
            return

        # Increment rotation angle by 90 degrees
        self.rotation_angle = (self.rotation_angle + 90) % 360

        # Redisplay the image with new rotation
        self.display_image()

    def create_placeholder(self):
        """Create a placeholder when no images are found"""
        self.root.geometry("400x300")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 300) // 2
        self.root.geometry(f"400x300+{x}+{y}")

        if hasattr(self, 'label'):
            self.label.destroy()

        self.label = tk.Label(
            self.root,
            text="No images found in pics folder\n(Supported: jpg, png)",
            bg='black',
            fg='white',
            font=('Arial', 14)
        )
        self.label.pack(fill=tk.BOTH, expand=True)
        self.root.configure(bg='black')

    def start_drag(self, event):
        """Start dragging the window"""
        # Check if click is on border (within 5 pixels of edge)
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        border_threshold = 5

        on_border = (
                event.x < border_threshold or
                event.x > width - border_threshold or
                event.y < border_threshold or
                event.y > height - border_threshold
        )

        if on_border:
            # Determine resize corner
            self.resizing = True
            if event.x < border_threshold and event.y < border_threshold:
                self.resize_corner = 'nw'
            elif event.x > width - border_threshold and event.y < border_threshold:
                self.resize_corner = 'ne'
            elif event.x < border_threshold and event.y > height - border_threshold:
                self.resize_corner = 'sw'
            elif event.x > width - border_threshold and event.y > height - border_threshold:
                self.resize_corner = 'se'
            elif event.x < border_threshold:
                self.resize_corner = 'w'
            elif event.x > width - border_threshold:
                self.resize_corner = 'e'
            elif event.y < border_threshold:
                self.resize_corner = 'n'
            elif event.y > height - border_threshold:
                self.resize_corner = 's'
        else:
            # Start dragging
            self.dragging = True
            self.resizing = False

        self.start_x = event.x_root
        self.start_y = event.y_root

    def on_drag(self, event):
        """Handle dragging or resizing"""
        if self.dragging:
            # Calculate new position
            dx = event.x_root - self.start_x
            dy = event.y_root - self.start_y

            x = self.root.winfo_x() + dx
            y = self.root.winfo_y() + dy

            self.root.geometry(f"+{x}+{y}")
            self.start_x = event.x_root
            self.start_y = event.y_root

        elif self.resizing:
            # Handle resizing
            dx = event.x_root - self.start_x
            dy = event.y_root - self.start_y

            current_x = self.root.winfo_x()
            current_y = self.root.winfo_y()
            current_width = self.root.winfo_width()
            current_height = self.root.winfo_height()

            new_x = current_x
            new_y = current_y
            new_width = current_width
            new_height = current_height

            if 'w' in self.resize_corner:
                new_x = current_x + dx
                new_width = current_width - dx
            if 'e' in self.resize_corner:
                new_width = current_width + dx
            if 'n' in self.resize_corner:
                new_y = current_y + dy
                new_height = current_height - dy
            if 's' in self.resize_corner:
                new_height = current_height + dy

            # Minimum size constraints
            min_width = 100
            min_height = 100

            if new_width < min_width:
                if 'w' in self.resize_corner:
                    new_x = current_x + current_width - min_width
                new_width = min_width

            if new_height < min_height:
                if 'n' in self.resize_corner:
                    new_y = current_y + current_height - min_height
                new_height = min_height

            self.root.geometry(f"{new_width}x{new_height}+{new_x}+{new_y}")
            self.start_x = event.x_root
            self.start_y = event.y_root

            # Resize current image to fit new window size
            self.resize_current_image(new_width, new_height)

    def stop_drag(self, event):
        """Stop dragging or resizing"""
        self.dragging = False
        self.resizing = False
        self.resize_corner = None

    def resize_current_image(self, new_width, new_height):
        """Resize the current image to fit the new window size"""
        if self.current_image is None:
            return

        try:
            # Apply rotation first
            img = self.current_image.copy()
            if self.rotation_angle != 0:
                img = img.rotate(-self.rotation_angle, expand=True)

            # Resize image to fit new window while maintaining aspect ratio
            img_width, img_height = img.size

            # Calculate scaling to fit within new dimensions
            ratio = min(new_width / img_width, new_height / img_height)
            new_img_width = int(img_width * ratio)
            new_img_height = int(img_height * ratio)

            img = img.resize((new_img_width, new_img_height), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)

            if hasattr(self, 'label'):
                self.label.configure(image=self.photo)
        except Exception as e:
            print(f"Error resizing image: {e}")

    def setup_resize_bindings(self):
        """Setup cursor changes on borders"""

        def on_enter(event):
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            border_threshold = 5

            if event.x < border_threshold and event.y < border_threshold:
                self.root.config(cursor="size_nw_se")
            elif event.x > width - border_threshold and event.y < border_threshold:
                self.root.config(cursor="size_ne_sw")
            elif event.x < border_threshold and event.y > height - border_threshold:
                self.root.config(cursor="size_ne_sw")
            elif event.x > width - border_threshold and event.y > height - border_threshold:
                self.root.config(cursor="size_nw_se")
            elif event.x < border_threshold:
                self.root.config(cursor="size_we")
            elif event.x > width - border_threshold:
                self.root.config(cursor="size_we")
            elif event.y < border_threshold:
                self.root.config(cursor="size_ns")
            elif event.y > height - border_threshold:
                self.root.config(cursor="size_ns")
            else:
                self.root.config(cursor="arrow")

        def on_leave(event):
            self.root.config(cursor="arrow")

        self.root.bind('<Motion>', on_enter)
        self.root.bind('<Leave>', on_leave)

    def exit_app(self, event=None):
        """Exit the application"""
        self.root.quit()
        self.root.destroy()
