from model import EmployeeModel
from view import EmployeeView
from controller import EmployeeController


def main():

    model = EmployeeModel()
    view = EmployeeView()

    controller = EmployeeController(
        model,
        view
    )

    controller.run()


if __name__ == "__main__":
    main()
