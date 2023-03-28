import textwrap

class text_decoration:


    @staticmethod
    #pass the variable 'message' so that the message can be called on itself rather than the instance 
    def story_banner(banner, message):
        # Calculate the width of the banner
        banner_width = 80

        # Break the message into multiple lines within the banner width
        message_lines = textwrap.wrap(message, banner_width - 4)

        # Create the banner string
        banner = banner * banner_width

        print(f"\n{banner}")
        for line in message_lines:
            print(f"{line:<{banner_width - 4}}  ")
        print(f"{banner}\n")


    @staticmethod
    def invalid_input(message):
        print(f"\nA!!! {message} !!!")


    @staticmethod
    def input_decorator(prompt, options):
        # Print prompt and options with fixed padding
        print(f"\n\n>>> {prompt} <<<\n")
        for option in options:
            print(f"{option}")
        print("\n")


    @staticmethod
    def center_message(message):
        print(f"{message}\n")


    @staticmethod
    def print_health(options):
        banner_width = 80
        banner = '*' * (banner_width // 2)
        print(f"{banner}\n")
        for i in range(0, len(options), 2):
            print(f"{options[i]} has {options[i+1]} health ♥")
        print(f"\n{banner}\n")


    @staticmethod
    def cavern_treasure():
        text_decoration.center_message("✰✰✰✰✰ you found treasure deep in the caverns! ✰✰✰✰✰")