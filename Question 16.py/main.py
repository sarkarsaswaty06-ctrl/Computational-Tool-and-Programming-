from model import StudentModel
from view import StudentView
from controller import StudentController


def main():
    model = StudentModel()
    view = StudentView()
    controller = StudentController(model, view)

    controller.run()


if __name__ == "__main__":
    main()
