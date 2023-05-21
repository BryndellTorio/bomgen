import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Integrated Micro-Electronics Inc. - Design and Development")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "imi_logo.png")), size=(26, 26))
        self.circuit_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "circuit_board_2.png")), size=(500, 150))
        self.excel_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "excel_icon.png")), size=(20, 20))
        self.file_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "file_icon.jpg")), size=(20, 20))
        self.imi_box_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "imi_box_logo.png")), size=(20, 20))
        self.information_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "information_icon.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  BOM Generator", image=self.imi_box_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.information_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Altium", "Cadence", "PADS"],
                                                                command=self.select_CAD_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.circuit_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=30, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Choose file", image=self.excel_image, compound="left")
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="logfile", image=self.file_image, compound="left")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def select_CAD_event(self, new_appearance_mode):
        # insert code to select the right command
        if new_appearance_mode == "Altium":
            print("Altium is selected.")
        elif new_appearance_mode == "Cadence":
            print("Cadence is selected.")
        elif new_appearance_mode == "PADS":
            print("PADS is selected.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
