from graphics import *

Progress = []
Trailer = []
Retriever = []
Excluded = []


def main_program():

    def get_input(user_input, input_error, invalid_value):
        credit_range = range(0, 140, 20)
        value = None

        while value is None or value not in credit_range:
            try:
                value = int(input(user_input))
            except ValueError:
                print(input_error)
                continue

            if value not in credit_range:
                print(invalid_value)

        return value

    def module_outcome():
        pass_credits = get_input("Please enter your credits at pass: ", "Integer required.", "Out of range.")
        defer_credits = get_input("Please enter your credits at defer: ", "Integer required.", "Out of range.")
        fail_credits = get_input("Please enter your credit at fail: ", "Integer required.", "Out of range.")

        total_credits = pass_credits + defer_credits + fail_credits  # calculate the total credits

        credit_data = [pass_credits, defer_credits, fail_credits]  # add input data to the list

        if total_credits != 120:  # check if the values entered are equal to 120
            print("Total incorrect.")
        elif pass_credits == 120:  # student's pass credits equal to 120 is Progress
            print("Progress")
            Progress.append(credit_data)  # add data to the Progress
        elif pass_credits == 100:  # student's pass credits equal to 100 is Progress(module trailer)
            print("Progress(module trailer)")
            Trailer.append(credit_data)  # add data to the Trailer
        elif fail_credits >= 80:  # student's fail credits equal or greater than to 80 is Exclude
            print("Exclude")
            Excluded.append(credit_data)  # add data to the Exclude
        else:
            print("Do not progress - module retriever")
            Retriever.append(credit_data)  # add data to the Retriever
        print()

    def display_histogram():
        win = GraphWin("Histogram", 568, 435)
        win.setBackground("white")

        heading = Text(Point(155, 25), 'Histogram Results')
        heading.draw(win)
        heading.setTextColor("#636363")
        heading.setSize(18)
        heading.setStyle("bold")

        categories = ["Progress", "Trailer", "Retriever", "Excluded"]
        data = [len(Progress), len(Trailer), len(Retriever), len(Excluded)]
        colors = ["#aafa9d", "#a0c689", "#a7bc77", "#d2b6b5"]

        bar_width = 110
        x_start = 50
        y_start = 340
        space_between = 6

        max_data = max(data)
        bar_scale = 270 / max_data  # Scales the bars to fit in the window
        total_outcomes = sum(data)  # Calculate the total outcomes

        for i in range(len(categories)):
            height = data[i] * bar_scale

            x_left = x_start + i * (bar_width + space_between)
            x_right = x_left + bar_width
            y_top = y_start - height

            rect = Rectangle(Point(x_left, y_start), Point(x_right, y_top))
            rect.setFill(colors[i])
            rect.setWidth(1)
            rect.setOutline("#81977e")
            rect.draw(win)

            label = Text(Point((x_left + x_right) / 2, y_start + 10), categories[i])
            label.setTextColor("#7b8995")  # Change text color
            label.setSize(13)  # Change text size
            label.setStyle("bold")  # Change text style
            label.draw(win)

            data_label = Text(Point((x_left + x_right) / 2, y_top - 10), str(data[i]))
            data_label.setTextColor("#7b8995")  # Change text color
            data_label.setSize(13)  # Change text size
            data_label.setStyle("bold")  # Change text style
            data_label.draw(win)

        total_text = Text(Point(170, 390), f"{total_outcomes} outcomes in total.")
        total_text.setTextColor("#7b8995")
        total_text.setSize(15)
        total_text.setStyle("bold")
        total_text.draw(win)

        x_axis_length = 500  # Set the length of the X-axis
        x_axis_start = 30  # Starting position of X-axis

        # Draw X-axis
        x_axis = Line(Point(x_axis_start, y_start), Point(x_axis_start + x_axis_length, y_start))
        x_axis.setFill("#81977d")
        x_axis.draw(win)

        try:
            win.getMouse()
            win.close()
        except GraphicsError:
            pass


    def print_module_data(list_name, lists):
        for item in lists:
            pass_credit = item[0]
            defer_credit = item[1]
            fail = item[2]
            print(list_name, "-", pass_credit, ",", defer_credit, ",", fail)

    def print_data_list():
        print_module_data("Progress", Progress)  # calling the print_module_data user defined function
        print_module_data("Progress (module trailer)", Trailer)
        print_module_data("Module retriever", Retriever)
        print_module_data("Exclude", Excluded)

    def write_module_data(list_name, lists, file):
        for item in lists:
            pass_credit = str(item[0])
            defer_credit = str(item[1])
            fail = str(item[2])
            file_data = list_name + "-" + pass_credit + "," + defer_credit + "," + fail
            file.write("%s\n" % file_data)  # writing file data to the text file

    def generate_text_file():
        print()
        name = input(
            "you can create a file to save your progression data,\nEnter a name for the file:  ")  # get file name
        file_name = (name + '.txt')  # create text file

        with open(file_name, 'w') as file:
            write_module_data("Progress", Progress, file)
            write_module_data("Trailer", Trailer, file)
            write_module_data("Retriever", Retriever, file)
            write_module_data("Excluded", Excluded, file)

        file.close()  # file close
        print("Your data has been saved to the file.Thank You!")

    user_status = input("Enter 'A' for staff or 'B' for student: ").upper()

    if user_status == 'A':
        module_outcome()
        print("Would you like to enter another set of data?")  # asking for another set of data
        choice = ""
        while choice.lower() != "q":
            choice = input(
                "Enter 'y' for yes or 'q' to quit and view results: ")  # asking user input only for choice of 'y' to
            # continue or 'q' to quit
            print()
            if choice.lower() == "y":  # giving user the option of choosing to add another student records
                module_outcome()
            elif choice.lower() == "q":  # giving user the option of choosing to display histogram,list and create text fil
                display_histogram()
                print_data_list()
                generate_text_file()
            else:
                continue

    elif user_status == 'B':
        module_outcome()
    else:
        print("Invalid choice. Please enter 'A' or 'B'.\n")
        main_program()

# main program
main_program()
